# code go here
# A simplified file which takes the old parts of bot build and stream lines them.
# Imports
import json
import os
import sys
import time
# JSON reading
    # Sets file path to JSONBuild rather than BotBuild
JSONBuildPath = f'{os.getcwd()}'.split('/')
JSONBuildPath.pop()
JSONBuildPath.append('JSONBuild/BotBuildInfo.json')
JSONBuildPath = '/'.join(JSONBuildPath)
    # Creating a dictionary to hold Json Data
BOTDict = {
    "asinNums": [],
    "asinUrls":[],
    "minPrice": [],
    "maxPrice": [],
    "userEmail": "placeHolder",
    "userPassword": "placeHolder"
}
# Opening and loading JSON data
pathOpen = open(JSONBuildPath)
jsonData = json.load(pathOpen)
# Storing the Item info data into BOTdict
dictCycles = 1
for items in jsonData["ItemINFO"]["Items"]:
    BOTDict["asinNums"].append(jsonData["ItemINFO"]["Items"][f"Item_{dictCycles}"]["ASIN_NUMBER"])
    BOTDict["minPrice"].append(jsonData["ItemINFO"]["Items"][f"Item_{dictCycles}"]["MIN_PRICE"])
    BOTDict["maxPrice"].append(jsonData["ItemINFO"]["Items"][f"Item_{dictCycles}"]["MAX_PRICE"])
    dictCycles += 1
# Storing the user info data into BOTdict
BOTDict["userEmail"] = jsonData["LoginFo"]["UserEmail"]
BOTDict["userPassword"] = jsonData["LoginFo"]["UserPassword"]
# Creating URLs from BOTdict data
    # Empty list to hold urls
urlList = []
     # Creating and adding urls to urlList
urlCycles = 0
baseURL = 'https://www.amazon.com/dp/'
for i in BOTDict["asinNums"]:
    BOTDict["asinUrls"].append(f'{baseURL}{BOTDict["asinNums"][urlCycles]}')
    urlCycles += 1
# defining path to chromedriver
chromeDriverPath = f'{os.getcwd()}'.split('/')
chromeDriverPath.pop()
chromeDriverPath.append('chromedriver')
chromeDriverPath = '/'.join(chromeDriverPath)
# defining the waitTime
waitTime = int(input('Input wait time between repetitions(3 seconds is recommended):'))
# importing selenium modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# importing beautifulsoup modules
from bs4 import BeautifulSoup
import requests
import re
# setting up selenium
chromeOptions = Options()
# Creating an service object for chromeDriverPath
serPath = Service(chromeDriverPath)
# Creates an instance of webdriver
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serPath, options=chromeOptions)
# Opening Amazon.com
driver.get('https://www.amazon.com/')
# Functions for bot algos
    # Checks the availability
def StockCheck():
    if driver.find_element(By.XPATH, '//*[@id="availability"]/span').text == 'In Stock.': # Finds the availibility text and returns boolean
        return True
    else:
        return False
    # Checks the price TODO : Figure price checker
def PriceCheck(minPrice, maxPrice, url):
    # Scrapes the price data from amazon
    headers = {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
    }
    website = requests.get(url, headers=headers)
    soup = BeautifulSoup(website.content, 'lxml')
    # Formating the price data
    price = soup.find('span', class_='a-offscreen').string
    price = list(price)
    price.remove(price[0])
    price = "".join(price)
    price = float(price)
    if minPrice < price < maxPrice:
        return True
    else:
        return False
# Product check loop
def ProductCheck():
    for url in BOTDict["asinUrls"]:
        print(f'Checking {url}')
        driver.get(url)
        time.sleep(waitTime)
        if StockCheck() and PriceCheck(minPrice=BOTDict["minPrice"][BOTDict["asinUrls"].index(url)], maxPrice=BOTDict["maxPrice"][BOTDict["asinUrls"].index(url)], url=url):
            driver.find_element(By.ID, 'add-to-cart-button').click()
            print(f'{url} added to cart!')
            sys.exit()
        else:
            print('Outside bot parameters, checking next...')
            pass
    return ProductCheck()
# Running product check loop
ProductCheck()
