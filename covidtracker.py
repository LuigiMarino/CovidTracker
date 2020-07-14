from bs4 import BeautifulSoup, NavigableString, Tag
import re
import requests
from datetime import date

today = date.today()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

r1 = requests.get("https://www.worldometers.info/coronavirus/country/uk/", headers=headers)
covidData = BeautifulSoup(r1.text, 'html.parser')

for body in covidData.body:
    if isinstance(body, NavigableString):
        continue
    if isinstance(body, Tag):
        print(body.text)    

covidData_Raw = ""

#covidData_TotalConfirmed
#covidData_DailyConfirmed
#covidData_TotalDeaths
#covidData_DailyDeaths
