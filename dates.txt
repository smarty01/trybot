# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:46:27 2019

@author: Shruti
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from translate import Translator


my_url="https://www.tourmyindia.com/kumbhmela/bathing-dates.html"
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
translator= Translator(to_lang="hi")

page_soup=soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"dates-details"})
#print(len(containers))

ans=""
occ_containers=containers[0].findAll("span",{"class":"kumbh-details"})
date_containers=containers[0].findAll("span",{"class":"kumbh-details-date"})
zipped=zip(occ_containers,date_containers)
for a,b in zipped:
    occ=a.text
    date=b.text
    final = occ + "-" + date
    
    translated=translator.translate(final)
    ans+=(final + "\n" + translated + "\n")
    #print(final + "|" + translated)
    
print(ans)        

    


     
    





