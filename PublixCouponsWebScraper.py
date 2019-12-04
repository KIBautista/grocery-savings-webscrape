#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Configure webdriver to use Chrome, set path to chromedriver

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe")

# Empty lists to store data of products

products = []
savings = [] 
coupon_expiration_date = []
driver.get("https://www.publix.com/savings/all-deals")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'content-wrapper'}):
    name=a.find('div', attrs={'class':'description text-block-default clamp-3'})
    savings=a.find('div', attrs={'class':'heading text-title-large display-none md-display-block'})
    coupon_expiration_date=a.find('div', attrs={'class':'validity text-block-default'})
    products.append(name.text)
    savings.append(savings.text)
    coupon_expiration_date.append(coupon_expiration_date.text) 

df = pd.DataFrame({'Product Name':products,'Savings':savings,'Coupon Expiration Date':expiration}) 
df.to_csv('grocery_coupons.csv', index=False, encoding='utf-8')
