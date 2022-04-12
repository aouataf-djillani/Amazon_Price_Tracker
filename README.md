# Amazon_Price_Tracker
 This automated Price Tracker for amazon product is built using Python. It allows Tracking price changes and sending email alerts once the desired price is reached 
## Steps 
- Sending request to get the html page from the url  
- Parsing the html page to extract infos: product name and price using bs4 (beautifulsoup) library 
- Comparing the price with the desired one 
- sending an e-mail alert using smtplib 

## Requirements and Setup  
### Chromedriver 

download and installation: https://chromedriver.chromium.org/getting-started
### Virtual Environment Setup 
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
### Requirements Installation 

```bash
pip install -r requirements.txt
```
### Runnig Price Tracker Script 
```bash
python3 scraper.py
```