# Copyright 2021, Jehu Morning, All rights reserved.
# TODO : add firefox support and test/add mac support
# Utlizing Selenium to construct the bot

# Importing variables TODO : Test whether importing from seperate .py files becomes a problem
import sys

from LoginCredentials import Username, Password
from ItemInfo import itemINFO_dict
from URL_Creation import urlList

# Importing modules
    # Selenium modules for bot automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
    # System modules for various uses
import os
import time

# Used in ProductCheck() to pause the function to increase time before stack overflow
waitTime = int(input('Input wait time between repetitions(3 seconds is recommended):'))

# Determines whether Bot runs headless
chromeOptions = Options()

# Path to Chrome Driver
serPath = Service(f'{os.getcwd()}\\chromedriver.exe')

# Creates an instance of webdriver
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions) # TODO :  Fix

# Opening Amazon.com
driver.get('https://www.amazon.com')

# TODO : Unlock this section in release draft
'''
# Signing in with LoginCredentials
    # Finds the signin prompt
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
    # Finds the username box, Sends username into input box
driver.find_element(By.ID, 'ap_email').send_keys(Username)
    # Clicks continue
driver.find_element(By.ID, 'continue').click()
    # Finds the password box, Sends password into input box
driver.find_element(By.ID, 'ap_password').send_keys(Password)
    # Clicks Submit
driver.find_element(By.ID, 'signInSubmit').click()
'''
# Function which finds product availability and return a Boolean
def StockCheck():
    if driver.find_element(By.XPATH, '//*[@id="availability"]/span').text == 'In stock.': # Finds the availibility text and returns boolean
        return True
    else:
        return False

# Function which finds product price, compares it to price params and returns a Boolean
def PriceCheck(minPrice, maxPrice, checkValue):
    price = int(driver.find_element(By.CLASS_NAME, 'a-price-whole').text)
    print(driver.find_element(By.CLASS_NAME, 'a-price-whole').text)
    if minPrice[checkValue] <= price and price <= maxPrice[checkValue]:
        return True
    else:
        return False

# Function which takes the product availability and cycles through until StockCheck() returns True
def ProductCheck():
    ProductCheck_cycles = 0
    ListItems = len(urlList) - 1 # Gets the number of items in the URL_List
    while ProductCheck_cycles <= ListItems: # Cycles through URL_list, opening, testing, and closing each url in loop
        driver.get(urlList[ProductCheck_cycles])
        print(f'Checking {urlList[ProductCheck_cycles]}...')
        time.sleep(waitTime) # Waits before starting calling StockCheck()
        if StockCheck() == True: # StockCheck() finds the availability of the item by scraping the html
            print(f'{urlList[ProductCheck_cycles]} is in stock!')
            time.sleep(waitTime)
            if PriceCheck(itemINFO_dict["MINPRICE"], itemINFO_dict["MAXPRICE"], ProductCheck_cycles) == True:
                driver.find_element(By.ID, 'add-to-cart-button').click() # Finds and clicks the Buy Now buttom
                sys.exit()
            else:
                print(f'{urlList[ProductCheck_cycles]} out of price range!')
                pass
        else:
            print(f'{urlList[ProductCheck_cycles]} is out of stock!')
            ProductCheck_cycles += 1
    if ProductCheck_cycles > (ListItems - 1): ProductCheck_cycles = 0 # Resets n after the last item in URL_list has been checked
    return ProductCheck()

# Calling the functions
ProductCheck()
