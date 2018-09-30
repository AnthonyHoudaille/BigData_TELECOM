#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:00:11 2018

@author: anthonyhoudaille
"""

import requests
from bs4 import BeautifulSoup


#Search = 'Acheter/Chaussures Kalenji'

def Moyenne_avis_Decathlon(query) :
    
    Tag = 'Acheter/'
    Recherche = str(query)
    Search = Tag + Recherche
    url = "https://www.decathlon.fr/"
    note_avis = [['moyenne', 'avis']]
    nbavis = 0
    moy = 0
    r = requests.get(url + Search)
    
    if r.status_code == 200 :
        
        
        html_doc = r.text
    
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        specific_class = 'thumbnail-link'
        class_moy_note = 'rating-note-container'
        class_nb_avis = 'review-count'
        class_title = 'title-product'
        all_links = list(map(lambda x : x['href'], soup.find_all("a", specific_class))) 
        for i in range(len(all_links)):
            
            url2 = all_links[i]                                        
    ##Permet de récupérer le nombre d'avis total et 
    #la moyenne des notes des utilisateurs
            r2 = requests.get(url+url2)
            html_doc2 = r2.text
                
            soup2 = BeautifulSoup(html_doc2, 'html.parser')
            
            avis = soup2.find("span", class_ = class_nb_avis).text
            moy_page = soup2.find("span", class_ = class_moy_note).text
            title = soup2.find("h1", class_ = class_title).text
            
            
#            moy_page = moy_page.replace(moy_page[-2:], '')
#            note_avis.append(list(map(float, [moy_page, avis])))
#            nbavis = nbavis + int(avis)
#            moy = moy + float(moy_page)
#        moyenne_globale = (moy / len(all_links))
        
        
    #print(all_links)  
    #print (url2)
    #    print (avis)
        print ("Le nombre d'avis total est de : " + str(nbavis))
        print ("la moyenne globale des chaussures est : " + str(moyenne_globale))
    #rs-global-rating #moyenne des notes (class)
    #rs-nb # nombre d'avis (class)