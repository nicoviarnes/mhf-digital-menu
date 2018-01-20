import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def scrapeRmh():
    index = open('index.html', 'w')
    baseURL = 'http://rockridgemarkethall.com'
    followURL = '/market-hall-foods/weekly-menu'
    req = urllib.request.Request(
        url= baseURL + followURL,
        data=None,
        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Referer': 'https://cssspritegenerator.com',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}
    )

    rmhWeeklyMenuList = urllib.request.urlopen(req)
    links = BeautifulSoup(rmhWeeklyMenuList, 'html.parser')
    currentMenuLink = links.find_all('h1', class_ = 'pos-title')[0]

    for a_tag in currentMenuLink('a', href=True):
        newUrl = a_tag['href']

    req2 = urllib.request.Request(
        url= baseURL + newUrl,
        data=None,
        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Referer': 'https://cssspritegenerator.com',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}
    )   

    rmhWeeklyMenuCurrent = urllib.request.urlopen(req2)
    menu = BeautifulSoup(rmhWeeklyMenuCurrent, 'html.parser')
    currentMenuTable = menu.find_all('div', class_ = 'menu')
    
    materializeCSS = '<link rel="stylesheet" type="text/css" href="css/materialize.min.css">\n\n'
    materializeJS = '\n\n<script type="text/javascript" src="js/materialize.min.js"></script>'
    jquery = '\n\n<script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>'
    altText = '<tr><th>Title/Description</th><th>Price</th></tr>'

    index.write(materializeCSS + str(currentMenuTable).strip('[]').replace(altText, '') + jquery + materializeJS)
    index.close()

scrapeRmh()