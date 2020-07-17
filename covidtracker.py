from bs4 import BeautifulSoup, NavigableString, Tag
import re
import requests
from datetime import date
import csv

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

#Strip out data and add to row entry
for a in covidData_MainCounter:
    a = (a.text.strip())
    rowEntry.append(removeComma(a))

#Field names
fields = ['Date', 'Total Cases', 'Total Deaths', 'Recovered']
#File name
filename = 'data.csv'

#With the file open, write the data
with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(rowEntry)

