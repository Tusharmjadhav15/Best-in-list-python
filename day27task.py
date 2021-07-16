from bs4 import BeautifulSoup
import requests
import csv


u ='https://authoraditiagarwal.com/'
url = requests.get(u)

soup = BeautifulSoup(url.text,'html.parser')

file1 = csv.writer(open('filexl.csv','w'))
file1.writerow(['scraping'])
file1.writerow([soup.title.text])

