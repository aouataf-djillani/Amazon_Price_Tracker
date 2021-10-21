import requests
from bs4 import BeautifulSoup
import time
import smtplib

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

headers = { "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"}

def alert_me(url,name, priceWanted):
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('aouataf.djillani@gmail.com','MyPassword')
    
    subject = 'Price fell down for '+name   
    body = 'Buy it now here: '+url   
    msg = f"Subject:{subject}\n\n{body}".encode('utf-8').strip()
    
    server.sendmail('aouataf.djillani@gmail.com','aouatefd@yahoo.com',msg)
    print('Email alert sent')    
    server.quit()

offer=[]
def trackPrice(url,priceWanted):
    
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html5lib")
    try:
        name= soup.find(id="productTitle").text.strip()
        price=float(soup.find(id="price_inside_buybox").text.strip().replace(',','').replace("€",""))
        if price<=priceWanted:
            offer.append(f"Great news !! You've got an offer on the {name} for {price}. Check out the product{url}")
            alert_me(url,name, priceWanted)
    except:
        offer.append("no details found on this product")
    return offer

url="https://www.amazon.fr/%C3%89lectrique-Montagne-Batterie-Engrenages-Kilom%C3%A9trage/dp/B08QN4KPKW/ref=sr_1_2?_encoding=UTF8&c=ts&dchild=1&keywords=V%C3%A9los+%C3%A9lectriques&qid=1634735179&s=sports&sr=1-2&ts_id=485936031"
#url=extract_url(url)
while True:
    print(trackPrice(url, 12999.0))
    time.sleep(60)

# to do :Run the program on AWS cloud