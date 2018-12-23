import bs4
from urllib.request import urlopen as uo
from bs4 import BeautifulSoup as bs

myurl = 'https://austin.craigslist.org/search/cta?query=mercedes'

uClient = uo(myurl)

# Opening page
pg_html = uClient.read()

# Closing page
uClient.close()

#HTML parsing
page_soup = bs(pg_html, "html.parser")

#car listing on craigslist
cars = page_soup.findAll(class_='result-row')

#total number of cars
totalcars = int(page_soup.find(class_='totalcount').text)

# function to get vehicle data from craigslist
def mercedes_results(x):
    print(cars[x].find(class_='result-title hdrlnk').text)
    print(cars[x].find(class_='result-price').text)
    print(cars[x].find(class_='result-title hdrlnk').get('href'))
    print('----------------------------------------------------')

#for loop used to print all cars onto the console
for car in range(0,totalcars):
    mercedes_results(car)
