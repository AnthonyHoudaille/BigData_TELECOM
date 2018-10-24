#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:47:12 2018

@author: anthonyhoudaille
"""

## lesson 4 : CLEANNING

#Enlever les espace d'une liste de string
String = "Alexandre ,   36 ans ,            live in Montreuil"
listS = String.split(',')
list2 = list(map( lambda x : String.strip([]), String[x]))
#Cacher certain numéro d'une carte bleue -- REGEX
