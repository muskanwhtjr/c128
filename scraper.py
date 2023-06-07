from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
import requests


start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/ssony/Downloads/PRO-C127-Student-Boilerplate-Code-main/PRO-C127-Student-Boilerplate-Code-main/chromedriver.exe")
time.sleep(10)
scraped_data=[]

def scrape(hyperlink):
    print(hyperlink)

    try:
        page=requests.get(hyperlink)
        soup= page.find_all("table")
        temp_list=[]
        for tr_tag in soup.find_all("tr"):
            td_tags= tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
                
                except:
                    temp_list.append("")
        
        scraped_data.append(temp_list)

    except:
        time.sleep(1)
        scrape(hyperlink)

        
    
    
    


stars_data=[]
for j in range(0,len(scraped_data)):
    stars_name=scraped_data[j][1]
    distance=scraped_data[j][3]
    mass=scraped_data[j][5]
    radius=scraped_data[j][6]
    lum=scraped_data[j][7]

    required_data=[stars_name,distance,mass,radius,lum]
    stars_data.append(required_data)

headers = ["stars_name","distance","mass","radius","lum"]
star_df_1=pd.DataFrame(stars_data,columns=headers)
star_df_1.to_csv('scrape_Data.csv',index=True,index_label="id")





