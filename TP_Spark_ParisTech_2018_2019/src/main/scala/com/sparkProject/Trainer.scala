package com.sparkProject

import org.apache.spark.SparkConf
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.ml.feature._
import org.apache.spark.ml.tuning.{ParamGridBuilder, TrainValidationSplit}
import org.apache.spark.sql.{DataFrame, SparkSession}


object Trainer {

  def main(args: Array[String]): Unit = {

    val conf = new SparkConf().setAll(Map(
      "spark.scheduler.mode" -> "FIFO",
      "spark.speculation" -> "false",
      "spark.reducer.maxSizeInFlight" -> "48m",
      "spark.serializer" -> "org.apache.spark.serializer.KryoSerializer",
      "spark.kryoserializer.buffer.max" -> "1g",
      "spark.shuffle.file.buffer" -> "32k",
      "spark.default.parallelism" -> "12",
      "spark.sql.shuffle.partitions" -> "12",
      "spark.driver.maxResultSize" -> "2g"
    ))

    val spark = SparkSession
      .builder
      .config(conf)
      .appName("TP_spark")
      .getOrCreate()


    /*******************************************************************************
      *
      *       TP 3
      *
      *       - lire le fichier sauvegarder précédemment
      *       - construire les Stages du pipeline, puis les assembler
      *       - trouver les meilleurs hyperparamètres pour l'entraînement du pipeline avec une grid-search
      *       - Sauvegarder le pipeline entraîné
      *
      *       if problems with unimported modules => sbt plugins update
      *
      ********************************************************************************/

    val df: DataFrame = spark
      .read
      .parquet("/Users/anthonyhoudaille/Desktop/TP_Spark_ParisTech_2018_2019/data/prepared_trainingset")

    //Creation of the pipeline. This one is compose by 10 stages.

    //First Stage : The goal is to split the text into words (or token)
    val tokenizer = new RegexTokenizer()
      .setPattern("\\W+")
      .setGaps(true)
      .setInputCol("text")
      .setOutputCol("tokens")

    //Second Stage : the goal is to remove all words we do not need (with no sense like "I" "the" ...)
    val removeWords = new StopWordsRemover()
      .setInputCol("tokens")
      .setOutputCol("filtered")

    // Third Stage : The goal is to determine the TF of each tokens and so create vectors
    val TFVector = new CountVectorizer()
      .setInputCol("filtered")
      .setOutputCol("TFfilted")

    // Fouth Stage : The goal is to rescale the feature vectors created below and store then into the column "tfidf"
    val idf = new IDF()
      .setInputCol("TFfilted")
      .setOutputCol("tfidf")

    // Fifth Stage : cast country2 in int  into a new column country_index
    val country_Indexer = new StringIndexer()
      .setInputCol("country2")
      .setOutputCol("country_indexed")
      .setHandleInvalid("keep")

    // Sixth Stage : cast country2 in int  into a new column country_index
    val currency_Indexer = new StringIndexer()
      .setInputCol("currency2")
      .setOutputCol("currency_indexed")

    // Seventh and eighth stages : the goal is to transform those index into "one-hot encoder"
    //maps a column of label indices to a column of binary vectors
    val country_Encoder = new OneHotEncoder()
      .setInputCol("country_indexed")
      .setOutputCol("country_onehot")

    val currency_Encoder = new OneHotEncoder()
      .setInputCol("currency_indexed")
      .setOutputCol("currency_onehot")

    //ninth stage : The goal is to join "tfidf", "days_campaign", "hours_prepa", "goal", "country_onehot", "currency_onehot"
    // into a new column "features"
    val features_Assembler = new VectorAssembler()
      .setInputCols(Array("tfidf", "days_campaign", "hours_prepa", "goal", "country_onehot", "currency_onehot"))
      .setOutputCol("features")

    //tenth stage : Classification Model : This is a logistical regression
    val logisticreg = new LogisticRegression()
      .setElasticNetParam(0.0)
      .setFitIntercept(true)
      .setFeaturesCol("features")
      .setLabelCol("final_status")
      .setStandardization(true)
      .setPredictionCol("predictions")
      .setRawPredictionCol("raw_predictions")
      .setThresholds(Array(0.7, 0.3))
      .setTol(1.0e-6)
      .setMaxIter(300)

    //Creation of the pipeline :

    val pipeline = new Pipeline()
      .setStages(Array(tokenizer,
        removeWords, TFVector, idf,
        country_Indexer, country_Encoder, currency_Indexer, currency_Encoder,
        features_Assembler, logisticreg))


    // Création of the tranning Data Set
    val Array(training, test) = df.randomSplit(Array(0.9, 0.1), seed = 12345)

    pipeline.fit(training)

    //Creation of the grid-search
    val paramGrid = new ParamGridBuilder()
      .addGrid(logisticreg.regParam, Array(10e-8, 10e-6, 10e-4, 10e-2))
      .addGrid(TFVector.minDF, Array(55.0, 75.0, 95.0))
      .build()

    val evaluator = new MulticlassClassificationEvaluator()
      .setLabelCol("final_status")
      .setPredictionCol("predictions")
      .setMetricName("f1")

    val trainValidationSplit = new TrainValidationSplit()
      .setEstimator(pipeline)
      .setEvaluator(evaluator)
      .setEstimatorParamMaps(paramGrid)
      // 70% of the data will be used for training and the remaining 30% for validation.
      .setTrainRatio(0.7)

    // Run train validation split, and choose the best set of parameters.
    val best_Model = trainValidationSplit.fit(training)

    // Creation of a new DF composed by predictions on our test Data Set (with the best set of parameters)
    val df_WithPredictions = best_Model
      .transform(test)
      .select("features", "final_status", "predictions", "raw_predictions")

    val f1_score = evaluator.evaluate(df_WithPredictions)

    printf("f1-score    " + f1_score + "\n \n")

    df_WithPredictions.groupBy("final_status", "predictions").count.show()


    println("hello world ! from Trainer")

  }
}
