import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def scrapeRmh():
    #pi path: /home/pi/Desktop/mhf-digital-menu/index.html
    #local path: /users/Nico/code/mhf-digital-menu/index.html
    index = open('/users/Nico/code/mhf-digital-menu/index.html', 'w')
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
    currentMenuTitle = menu.find_all('h1', class_ = 'pos-title')[0]
    currentMenuDate = menu.find_all('h2', class_ = 'pos-subtitle')[0]

    autoRefresh = '<META HTTP-EQUIV="refresh" CONTENT="500">\n\n'    
    scripts = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">\n\n<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>\n\n<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>\n\n<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>\n\n'
    altText = '<tr><th>Title/Description</th><th>Price</th></tr>'
    trBugs = '<tr></tr>'

    tableNoStyle = '<table id="weekly-menu">'
    tableStyled = '<table id="weekly-menu" class="table table-dark" style="font-size: 20px">'
    removeBoldOpen = '<strong>'
    removeBoldClose = '</strong>'
    h4NoStyle = '<h4>'
    h4Styled = '<h4 style="font-size: 40px">'

    h1NoStyle = '<h1 class="pos-title">'
    h1Styled = '<div style="background-color: #cc3300"><h1 class="pos-title" style="text-align: center; color: white; font-size: 40px">'

    h2NoStyle = '<h2 class="pos-subtitle">'
    h2Styled = '<h2 class="pos-subtitle" style="text-align: center; color: white; font-size: 32px">'
    unclosedHeaderDiv = '</h2>'
    closedHeaderDiv = '</h2></div>'

    divOpen = '<div style="display: block; overflow: auto; height: 100%; background-color: #32383e">\n\n'
    divClose = '</div>'

    MENU_HTML = autoRefresh + scripts + divOpen + str(currentMenuTitle).replace(h1NoStyle, h1Styled) + str(currentMenuDate).replace(h2NoStyle, h2Styled).replace(unclosedHeaderDiv, closedHeaderDiv) + str(currentMenuTable).strip('[]').replace(altText, '').replace(trBugs, '').replace(tableNoStyle, tableStyled).replace(removeBoldOpen, '').replace(removeBoldClose, '').replace(h4NoStyle, h4Styled) + divClose

    index.write(MENU_HTML)
    index.close()

scrapeRmh()
