#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:13:11 2018

@author: anthonyhoudaille
"""

# Données Tabulaires

import numpy as np
import pandas as pd
import re

#format pivot


releves = [
            ['lundi', 'temperature', 28]
            ,['lundi', 'ensoleillement', 4]
            ,['lundi', 'pollution', 5]
            ,['lundi', 'pluie', 100]
            ,['mardi', 'temperature', 28]
            ,['mardi', 'ensoleillement', 4]
            ,['mardi', 'pollution', 5]
            ,['mardi', 'pluie', 100]
            ,['mercredi', 'temperature', 28]
            ,['mercredi', 'ensoleillement', 4]
            ,['mercredi', 'pollution', 5]
            ,['mercredi', 'pluie', 100]
            ,['jeudi', 'temperature', 28]
            ,['jeudi', 'ensoleillement', 4]
            ,['jeudi', 'pollution', 5]
            ,['jeudi', 'pluie', 100]
            ,['vendredi', 'temperature', 28]
            ,['vendredi', 'ensoleillement', 4]
            ,['vendredi', 'pollution', 5]
            ,['vendredi', 'pluie', 100]
           ]

df = pd.DataFrame(releves, columns = ['day', 'metric', 'value'])
df_wide = df.pivot(index = 'day', columns = 'metric', values = 'value')

pd.melt(df_wide.reset_index(),['day'],['ensoleillement'],['pluie'], ['pollution'], ['temperature'])
print(df.head(2))
print(df_wide.head(2))

#df.set_index('day').ix['mardi'] permet de selectionner seulement les lignes de day=mardi

            