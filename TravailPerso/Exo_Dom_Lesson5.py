#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 23:41:56 2018

@author: anthonyhoudaille
"""

#2016-Densité.csv
#Spécialistes-Honoraires2016.csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Density2016 = pd.read_csv("2016-Densité.csv", sep=';', header = None)

headDensity = Density2016.iloc[0, : ]
oldheadDensity = Density2016.columns
Density2016 = Density2016.iloc[1 :, : ]
Density2016.rename(columns = dict(zip(oldheadDensity, headDensity)), inplace= True)
print(Density2016.head(5))

UsefullDataDensity = Density2016[['Départements', 'Départements nom', 'Total H+F', 'Superficie (km2)']].reset_index()
print(UsefullDataDensity.info())


Honoraires2016 = pd.read_csv("Spécialistes-Honoraires2016.csv", error_bad_lines=False,sep=';', header = None)

head = Honoraires2016.iloc[0, : ]
oldhead = Honoraires2016.columns
TotalSpécialistes = Honoraires2016.loc[Honoraires2016[0]=="TOTAL SPECIALISTES", : ]
TotalSpécialistes.rename(columns = dict(zip(oldhead, head)), inplace= True)

print(TotalSpécialistes.info())
UsefullDataHonoraires = TotalSpécialistes[['DEPARTEMENT', 'EFFECTIFS', 'DEPASSEMENTS (Euros)']].reset_index()

UsefullDataDensity['Total H+F'] = UsefullDataDensity['Total H+F'].apply(lambda x: x.replace('\xa0', '')).astype(float)
UsefullDataDensity['Superficie (km2)'] = UsefullDataDensity['Superficie (km2)'].apply(lambda x: x.replace('\xa0', '')).astype(float)

UsefullDataHonoraires['EFFECTIFS'] = UsefullDataHonoraires['EFFECTIFS'].apply(lambda x: x.replace('\xa0', '').replace('nc', '0')).astype(float)

UsefullDataHonoraires['DEPASSEMENTS (Euros)'] = UsefullDataHonoraires['DEPASSEMENTS (Euros)'].apply(lambda x: x.replace('\xa0', '').replace('nc', '0')).astype(float)


Density = (UsefullDataHonoraires['EFFECTIFS']/UsefullDataDensity['Total H+F']) 
MeanDepassement = (UsefullDataHonoraires['DEPASSEMENTS (Euros)']   / UsefullDataHonoraires['EFFECTIFS']) / np.mean(UsefullDataHonoraires['DEPASSEMENTS (Euros)']) * 100 

NewDF = pd.concat([UsefullDataHonoraires.iloc[:, 1], Density, MeanDepassement], axis = 1)
oldheadnewDF = NewDF.columns
headnewDF = ['Département','Densité de médecin','Dépassement moyen']
NewDF.rename(columns = dict(zip(oldheadnewDF, headnewDF)), inplace= True)
NewDF = NewDF.drop([ 96, 102,103], axis = 0)

print(NewDF.head())

plt.figure(figsize=(5,5))
plt.scatter(NewDF['Densité de médecin'],NewDF['Dépassement moyen'])
axes = plt.gca()
axes.set_xlim(0, 0.010)
axes.set_ylim(0, 0.15)
plt.xlabel("Densité de médecin ")
plt.ylabel("Dépassement moyen en %")
plt.title("Courbe representative  du Dépassement moyen d'honoraires en fonction de la densité de médecin ")
plt.show()


#Merger les DF. Pour cela utiliser "slugify"
#str.pad checker ce que c'est: permet d'avoir le même nombre de chiffres sur une colonne
#lire pd.merge() très important

