"""

Updates: the data is being loaded dynamically with JavaScript, presumably from a database / API. 
Check and use newscraper.py  where we use Selenium to fetch dynamically loaded data.
"""


import requests
from bs4 import BeautifulSoup
import time
import smtplib
import local_settings
# Having the asin is enough to get to a product ppage on Amazon
# Extracts it and returns a shorter version of it : eg https://www.amazon.fr/dp/B08QN4KPKW 
def extract_url(url):

    if url.find("www.amazon.fr") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.fr" + url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.fr" + url[index:index2]
            else:
                url = None
    else:
        url = None
    return url

# including the headers to avoid blocked request 
headers = { "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"}
# Sends an email alert once the product reaches the desired price
def alert_me(url,name, priceWanted):
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('aouataf.djillani@gmail.com',local_settings.MAIL_PASSWORD)
    
    subject = 'Price fell down for '+name   
    body = 'Buy it now here: '+url   
    msg = f"Subject:{subject}\n\n{body}".encode('utf-8').strip()
    
    server.sendmail('aouataf.djillani@gmail.com','aouatefd@yahoo.com',msg)
    print('Email alert sent')    
    server.quit()
# Sends a request
# parses the html page with beautifulsoup 
# compares the price with the desired price
def trackPrice(url,priceWanted):

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "lxml")
    try:
        name= soup.select(id="productTitle").text.strip()
        
        price=float(soup.find('span',attrs={"class":"a-price a-text-price a-size-medium apexPriceToPay"}).text.strip().replace(',','').replace("€",""))
        print(price)
        if price<=priceWanted:
            alert_me(url,name, priceWanted)
    except:
        print("no details found on this product")
    return offer

url="https://www.amazon.com/Acer-Predator-PH315-54-760S-i7-11800H-Keyboard/dp/B092YHJLS6/ref=sr_1_6?crid=F1JXNBNMFGGU&keywords=gamer+laptop&qid=1649613915&s=computers-intl-ship&sprefix=gamer+laptop+%2Ccomputers-intl-ship%2C176&sr=1-6"

print(trackPrice(url, 12999.0))

# to do :Run the program on AWS cloud
# cron(08**?*) every day at 8 am 

