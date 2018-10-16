#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 08:52:51 2018

@author: anthonyhoudaille
"""
import pandas as pd
import numpy as np
import scipy.stats as stat
import math as mp
import matplotlib.pyplot as plt
from sklearn import  linear_model
from mpl_toolkits.mplot3d import Axes3D
import statsmodels.regression.linear_model as sm

## Exercice 1 
##Question 1

def TP2():
    ##Question 1
    df = pd.read_csv("invest.txt", sep = ' ')
    print(df.head())
    
    ##Question 2
    ## nuage de points 
            #df.plot.scatter(x='gnp',y='invest')
            #plt.xscale('log')
            #plt.yscale('log')
    
    #mise à l'échelle log
    df['gnp'] = np.log(df['gnp'])
    df['invest'] = np.log(df['invest'])
    df.plot.scatter(x='gnp',y='invest', label ='echelle log')
    plt.show()
    
    
    ##Question 3
    
    Y_ = df['invest'].mean()
    X = df['gnp']
    X_ = df['gnp'].mean()
    Y = df['invest']
    
        ##Methode 1: utilisation des for (pas optimal)
        #for i in range(len(df['invest'])) :
            #numerateur = numerateur + (Y[i] - Y_)*(X[i] - X_) 
            #denominateur = denominateur + ((X[i] - X_)**2)
            
        ## Méthode 2 : utiliser .sum()
    pente = ((Y - Y_)*(X - X_)).sum() / ((X - X_)**2).sum()
    intercept = Y_ - pente * X_
    
    print (pente)
    print(intercept)
    
        ## Ecart type
    n = len(X)
    sigmahat = mp.sqrt((1 / (n - 2)) * ((Y - (intercept + pente * X))**2).sum())
    print (sigmahat)
    
    sigma_intercept = sigmahat * mp.sqrt( (1 / n) + X_**2  / ((X - X_)**2).sum() )
    print (sigma_intercept)
    
    sigma_pente = sigmahat * mp.sqrt( 1  / ((X - X_)**2).sum() )
    print (sigma_pente)
        ## Coeff de détermination
    Yhat = intercept + pente * X
    R2 = 1 - (((Y - Yhat)**2).sum() / ((Y - Y_)**2).sum())
    
    print (R2)
    
    ##Question 4 
        #On veut déterminer si l'hypothèse pente=0 est vrai ou non
        # Pour cela, on détermine la statistique du test de student et sa p-value
        
    StatistiqueZ = pente / sigma_pente
    print (StatistiqueZ)
    #Z = 18, on rejette donc l'hypothèse pente = 0
    
    # déterminons la p-value 
    pval = stat.t.sf(np.abs(StatistiqueZ), n-2)*2
    print (pval)
    
    #Z = 18>>pval, on rejette donc l'hypothèse pente = 0
    
    ##Question 5
    
    Invest_predict = mp.log(intercept + pente * 1000)
    print(Invest_predict)
    
    
    vals = stat.t.ppf(0.9,  n-2)
    print(vals)
    sigma3 =  sigmahat * np.sqrt( (1 / n) + ((X - X_)**2)  / ((X - X_)**2).sum() )
    sigma4 =  sigmahat * np.sqrt( 1 + (1 / n) + (X - X_)**2  / ((X - X_)**2).sum() )
    
    #besoin de mettre np.sqrt pour obtenir une série d'intervalle de confiance
    IC = [Invest_predict - (vals * sigma3) , Invest_predict + (vals * sigma3) ]
    print (IC)
    
    IC2 = [Invest_predict - (vals * sigma4) , Invest_predict + (vals * sigma4) ]
    print (IC2)
    
    ##Question 6
    
    df.plot.scatter(x='gnp',y='invest')
    plt.plot(X, intercept + pente * X, label = 'regressionLine')
    plt.plot(X, intercept + pente * X + (vals * sigma3), label = 'CImax')
    plt.plot(X, intercept + pente * X - (vals * sigma3), label = 'CImin')
    plt.plot(X, intercept + pente * X + (vals * sigma4), label = 'PImax')
    plt.plot(X, intercept + pente * X - (vals * sigma4), label = 'PImin')
    plt.xlabel('gnp (log)')
    plt.ylabel('invest (log)')
    plt.legend()
    plt.show()
    
    ## Question 7 
        

        #Creation of the linearRegression object
    regLin = linear_model.LinearRegression()
    
        #Train the model with train sets
    #regLin.fit(gnp_train, invest_train)
    regLin.fit(X[: , np.newaxis], Y)
        
    invest_predict_GNp1000 = np.log(regLin.predict(1000))
    
        #Coefficient 
    Coef = regLin.coef_
    InTercept = regLin.intercept_
    print(invest_predict_GNp1000[0])
    print(Coef)
    print(InTercept)
    
    ##Question 8
    
            # Creation of a test set
    X_test = np.linspace(np.min(X), np.max(X), 15)
    
            #Make predictions using testing sets
    invest_predict = regLin.predict(X_test[: , np.newaxis])
    
    df.plot.scatter(x='gnp',y='invest')
    plt.plot(X, invest_predict, color='red', label = 'prediction of invest')
    plt.plot(X, InTercept + Coef * X, label = 'regressionLine', color = 'green')

    plt.plot(np.log(1000), InTercept + Coef * invest_predict_GNp1000 , \
             marker = "X", color= 'black',  \
             label = 'Predicted Invest for GNP = 1000') 
    plt.xlabel('gnp (log)')
    plt.ylabel('invest (log)')
    plt.legend()
    plt.show()
    
    #Question 9
    
    X = np.hstack([np.ones(shape = (len(Y),1)), df[['gnp', 'interest']]])
    Xt = np.transpose(X)
    Gram_hat = np.matmul(Xt , X) 
    
        #Pour determiner si la matrice est de rang plein il faut quelle soit 
        #inversible: 
            # ie: symétrique
            # et vap différent de 0
    
    print("Test de symétrie : " + str(Gram_hat[1,0]==Gram_hat[0,1]))
   
    vap = np.linalg.eig(Gram_hat)[0]
    print("Les valeurs propres de la matrice de gram sont : " + str(vap)+ "\n \
          On remarque qu'elles ne sont pas nulle \nDonc la matrice de Gram est\
          de rang plein. \n \n \n")
    
    #Question 10
    Y = np.hstack(df['invest'])
    gram_inv = np.linalg.inv(Gram_hat)
    
        #Determinons les coefficients de beta
    beta_hat = np.matmul(gram_inv, np.matmul(Xt, Y))
    print("Les trois coefficient sont les suivants : " + str(beta_hat))
    
        #Determinons leurs variances :
    sigbeta0 = mp.sqrt((sigmahat**2) * gram_inv[0,0])
    sigbeta1 = mp.sqrt((sigmahat**2) * gram_inv[1,1])
    sigbeta2 = mp.sqrt((sigmahat**2) * gram_inv[2,2])
    print("L'écart-type du coefficient beta0 est : " + str(sigbeta0))
    print("L'écart-type du coefficient beta1 est : " + str(sigbeta1))
    print("L'écart-type du coefficient beta2 est : " + str(sigbeta2))
    
        # Coeff de détermination
    Yhat = np.matmul(X, beta_hat)
    R2 = 1 - (((Y - Yhat)**2).sum() / ((Y - Y_)**2).sum())
    print ("Le nouveau coeff de détermination est de : " + str(R2))
    
        # Pour beta 0
        
            #Statistique de test
    StatistiqueZb0 = beta_hat[0] / sigbeta0
    print ("La Statistique de test de beta 0 est : " + str(StatistiqueZb0))
    
            # déterminons la p-value 
    pvalb0 = stat.t.sf(np.abs(StatistiqueZb0), n-3)*2
    print ("La p-value de beta0 est : " + str(pvalb0))
    
        # Pour beta 1
        
            #Statistique de test
    StatistiqueZb1 = beta_hat[1] / sigbeta1
    print ("La Statistique de test de beta 1 est : " + str(StatistiqueZb1))
    
            # déterminons la p-value 
    pvalb1 = stat.t.sf(np.abs(StatistiqueZb1), n-3)*2
    print ("La p-value de beta1 est : " + str(pvalb1))
    
        # Pour beta 2
        
            #Statistique de test
    StatistiqueZb2 = beta_hat[2] / sigbeta2
    print ("La Statistique de test de beta 2 est : " + str(StatistiqueZb2))
    
            # déterminons la p-value 
    pvalb2 = stat.t.sf(np.abs(StatistiqueZb2), n-3)*2
    print ("La p-value de beta0 est : " + str(pvalb2) +"\n \n \n")
    
        ##Question 11
    
    x = np.hstack([1, np.log(1000), 10])    
    predicted_invest = np.matmul(x, beta_hat)
    print((predicted_invest))
    
    valstest = stat.t.ppf(0.999,  n-2)
    sigpredict = np.matmul(np.transpose(x), np.matmul(gram_inv, x))
    
            #Interval de prédiction
    Ip = [predicted_invest - (valstest * sigmahat * mp.sqrt(1 + sigpredict)) ,\
          predicted_invest + (valstest * sigmahat * mp.sqrt(1 + sigpredict)) ]
    
            #Interval de confiance
    Ic = [predicted_invest - (valstest * sigmahat * mp.sqrt(sigpredict)) , \
          predicted_invest + (valstest * sigmahat * mp.sqrt(sigpredict)) ]
    
    print("l'intervalle de prédiction est : \n      "+  str(Ip))
    print("l'intervalle de confiance est : \n      "+  str(Ic)+"\n \n")
    
    #Question 12
    
    
    
    
    x_surf, y_surf = np.meshgrid(np.linspace(df.gnp.min(), df.gnp.max(), 100),\
                        np.linspace(df.interest.min(), df.interest.max(), 100)) 
    #onlyX = pd.DataFrame({'gnp (log)': x_surf.ravel(), 'interest ': y_surf.ravel()})
   
    Z = beta_hat[0] + beta_hat[1] * x_surf + beta_hat[2] * y_surf
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['gnp'],df['invest'],df['interest'],c='blue', marker='o', alpha=0.5)
    ax.plot_surface(x_surf,y_surf, Z.reshape(x_surf.shape) , color='red', alpha=0.5)
    
    ax.plot_surface(x_surf,y_surf, (Z + Ip[0]).reshape(x_surf.shape) , color='green', alpha=0.3)
    ax.plot_surface(x_surf,y_surf, (Z - Ip[1]).reshape(x_surf.shape) , color='yellow', alpha=0.3)
    
    ax.plot_surface(x_surf,y_surf, (Z - Ip[0]).reshape(x_surf.shape) , color='black', alpha=0.3)
    ax.plot_surface(x_surf,y_surf, (Z + Ic[1]).reshape(x_surf.shape) , color='purple', alpha=0.3)
    
    ax.set_xlabel('gnp (log)')
    ax.set_ylabel('interest')
    ax.set_zlabel('invest (log)')
    plt.show()
    
    
    #Question 13
    
    #En utilisant le paclage sm.OLS, on estime les paramètres puis on les teste 1 à 1
    results = sm.OLS(Y, X).fit().params
    print("Beta 0 vaut : " "%.3f" % results[0])
    print("Beta 1 veut : " "%.3f" % results[1])
    print("Beta 2 vaut : " "%.3f" % results[2])
    