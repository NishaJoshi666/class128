import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)
planet_data = []
def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

def scrapemoredata(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content,'html.parser')
    newplanetdata = []
    for trtag in soup.find_all('tr',attrs={'class':'fact_row'}):
        tdtags = trtag.find_all('td')
        templist = []
        for td in tdtags:
            try:
                templist.append(td.find_all('div',attrs={'class':'value'})[0].content[0])
            except:
                templist.append('')
        newplanetdata.append(templist)
    pass

scrape()
for index,data in enumerate(planet_data):
# for data in planet_data:
    scrapemoredata(data[5])
    