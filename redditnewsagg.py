import bs4
from urllib.request import urlopen as uo
from bs4 import BeautifulSoup as soup

url = 'https://www.reddit.com/r/news'

client = uo(url)

html = client.read()
pgsoup = soup(html,"html.parser")

#Grabbing headlines and URLs from Reddit
header = pgsoup.findAll(class_='imors3-0 iuScIP')
link = pgsoup.findAll(class_='b5szba-0 iUAolq')

# Function used to print out headlines and links while skipping ads on Reddit
def news(x):
    headline = header[x].get_text()
    newslink = link[x].get('href')
    if 'alb.reddit' in newslink:
        print('***')
    else:
        print(headline)
        print('Link: '+newslink)
        print('----------------------------------------')

#Printing the maximum amount of articles onto the console
for x in range(0,28):
    news(x)
