#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:00:11 2018

@author: anthonyhoudaille
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#Search = 'Acheter/Chaussures Kalenji'

def moyenne_avis_Decathlon(Query):
    
    Tag = 'Acheter/'
    Recherche = Query
    Search = Tag + Recherche
    url = "https://www.decathlon.fr/"
    
    listnbavis =[]
    listmean =[]
    listtitle =[]
    listprice =[]
   
    
   
    
    r = requests.get(url + Search)
    
    if r.status_code == 200 :
        
        
       # html_doc = r.text
    
        #soup = BeautifulSoup(html_doc, 'html.parser')
        
        ##find the page 2 and take the HTLM page
        ## Explaination : On this site, there is no pages but juste one we can extend
        ## but for same reason, if I want to write page3 or page6 the search will put page2....
        specific_class = 'thumbnail-link'
        
        #class_page2_articles ="cta blue btn_show_next_product right"
        #nb_article = soup.find("a", class_=class_page2_articles)['href']
        
        ##I'm getting all url disponible for my query
        #if (nb_article != None):
         #   rp2 = requests.get(url + nb_article)
         #   html_p2 = rp2.text
        #    soup_p2 = BeautifulSoup(html_p2, 'html.parser')
         #   all_links = list(map(lambda x : x['href'], soup_p2.find_all("a", specific_class)))
        #else :
        nbpage=[1,2]
        for page in nbpage  :
            Tag2 = "#page"
            rp2 = requests.get(url+ Search + Tag2+ str(page))
            html_p2 = rp2.text
            soup_p2 = BeautifulSoup(html_p2, 'html.parser')
            all_links = list(map(lambda x : x['href'], soup_p2.find_all("a", specific_class)))
        ##Declaration of my differents classes
        
            class_moy_note = 'rating-note-container'
            class_nb_avis = 'review-count'
            class_title = 'title-product'
            class_price = 'price'
        
        
        

            for link in range(len(all_links)):
                url2 = all_links[link]                                        
                ##Area which permit to store all relevant informations into a CSV
                r2 = requests.get(url+url2)
                html_doc2 = r2.text
                
                soup2 = BeautifulSoup(html_doc2, 'html.parser')
                ##Creation of my array of numbrer of comment for the article
                avis = soup2.find("span", class_ = class_nb_avis)
                if (avis != None):
                    
                    listnbavis.append(avis.text)
                else :
                    listnbavis.append("n/a")
                        
                    ##Creation of my array of globalmean for the article
                moy_page = soup2.find("span", class_ = class_moy_note)
                if (moy_page != None):
                    listmean.append(moy_page.text)
                else :
                    listmean.append("n/a")
                        
                    ##Creation of my array of title of articles
                title = soup2.find("h1", class_ = class_title)
                if (title != None):
                    listtitle.append(title.text)
                else :
                    listtitle.append("n/a")
                    
                price = soup2.find("div", class_= class_price)
                listprice.append(price.text.replace("*",""))
            
            
        df = pd.DataFrame(np.stack((listtitle, listnbavis, listmean, listprice), axis = 0).transpose(), columns = ["Title", "number of Comment", "Mean", "Price"])
        df.head()
        
        df.to_csv(Query + ".csv" )
    
    #print(all_links)  
    #print (url2)
    #    print (avis)
        ##print ("Le nombre d'avis total est de : " + )
        print ("end of the prog")
