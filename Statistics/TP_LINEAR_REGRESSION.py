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
    
    Invest_predect = mp.log(intercept + pente * 1000)
    print(Invest_predect)
    
    
    vals = stat.t.ppf(0.9,  n-2)
    print(vals)
    sigma3 =  sigmahat * np.sqrt( (1 / n) + ((X - X_)**2)  / ((X - X_)**2).sum() )
    sigma4 =  sigmahat * np.sqrt( 1 + (1 / n) + (X - X_)**2  / ((X - X_)**2).sum() )
    
    #besoin de mettre np.sqrt pour obtenir une série d'intervalle de confiance
    IC = [Invest_predect - (vals * sigma3) , Invest_predect + (vals * sigma3) ]
    print (IC)
    
    IC2 = [Invest_predect - (vals * sigma4) , Invest_predect + (vals * sigma4) ]
    print (IC2)
    
    ##Question 6
    
    df.plot.scatter(x='gnp',y='invest', label ='echelle log')
    plt.plot(Yhat, intercept + pente * X)
    plt.show()
    
    
    