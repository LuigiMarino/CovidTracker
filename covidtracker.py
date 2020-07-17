from bs4 import BeautifulSoup, NavigableString, Tag
import re
import requests
from datetime import date
import csv
import pandas as pd

#Todays Date
today = date.today()

#Row Data
rowEntry = [str(today)]
#Row Headers
emailMessageHeaders = ['Coronavirus Cases', 'Deaths', 'Recovered']

#Browser Headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

#Get webpage
r1 = requests.get("https://www.worldometers.info/coronavirus/country/uk/", headers=headers)
covidData = BeautifulSoup(r1.text, 'html.parser')

#Get Data from webpage
covidData_MainCounter = covidData.find_all('div', attrs={'class' : 'maincounter-number'})

#Function to remove comma
def removeComma(b):
    return b.replace(',', '')

#Field names
fields = ['Date', 'Total Cases', 'Total Deaths', 'Recovered', 'Daily Cases', 'Daily Deaths']
#File name
filename = 'data.csv'

#Fucking with the data
df = pd.read_csv(filename)
covidData_TotalCases = df['Total Cases']
covidData_TotalDeaths = df['Total Deaths']


#print("Daily Cases: " + str(covidData_DailyCases))
#print("Daily Deaths: " + str(covidData_DailyDeaths))

#Strip out data and add to row entry
for a in covidData_MainCounter:
    a = (a.text.strip())
    rowEntry.append(removeComma(a))

covidData_DailyCases = int(rowEntry[1]) - df['Total Cases'].iat[-1]
covidData_DailyDeaths = int(rowEntry[2]) - df['Total Deaths'].iat[-1]

rowEntry.append(covidData_DailyCases)
rowEntry.append(covidData_DailyDeaths)

#With the file open, write the data
with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(rowEntry)