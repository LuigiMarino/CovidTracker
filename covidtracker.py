from bs4 import BeautifulSoup, NavigableString, Tag
import re
import requests
from datetime import date

today = date.today()
emailMessageHeaders = ['Coronavirus Cases', 'Deaths', 'Recovered']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

r1 = requests.get("https://www.worldometers.info/coronavirus/country/uk/", headers=headers)
covidData = BeautifulSoup(r1.text, 'html.parser')

covidData_MainCounter = covidData.find_all('div', attrs={'class' : 'maincounter-number'})

i = 0

#print("Corona Virus Cases")
for a in covidData_MainCounter:
    print(emailMessageHeaders[i])
    print(a.text.strip())
    i += 1

#covidData_TotalConfirmed
#covidData_DailyConfirmed
#covidData_TotalDeaths
#covidData_DailyDeaths
