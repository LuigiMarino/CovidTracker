from bs4 import BeautifulSoup, NavigableString, Tag
import re
import requests
from datetime import date
import csv

today = date.today()
rowEntry = [str(today)]
emailMessageHeaders = ['Coronavirus Cases', 'Deaths', 'Recovered']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

r1 = requests.get("https://www.worldometers.info/coronavirus/country/uk/", headers=headers)
covidData = BeautifulSoup(r1.text, 'html.parser')

covidData_MainCounter = covidData.find_all('div', attrs={'class' : 'maincounter-number'})

def removeComma(b):
    return b.replace(',', '')

for a in covidData_MainCounter:
    a = (a.text.strip())
    rowEntry.append(removeComma(a))

print(rowEntry)
#Field names
fields = ['Date', 'Total Cases', 'Total Deaths', 'Recovered']
#File name
filename = 'data.csv'

with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    #csvwriter.writerow(fields)
    csvwriter.writerow(rowEntry)


#covidData_TotalConfirmed
#covidData_DailyConfirmed
#covidData_TotalDeaths
#covidData_DailyDeaths
