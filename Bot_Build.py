# Utlizing Selenium to construct the bot

# Importing variables
from BotFiles.LoginCredentials import Username, Password
from BotFiles.ItemInfo import values

# Importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
import time
import sys

# Time variable (adjustable)
x = 1

# Path to Chrome Driver
driver_path = os.getcwd() + '\\ChromeDriver\\chromedriver.exe'
ser_path = Service(driver_path)

# Creates an instance of webdriver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ser_path, options=chrome_options)

# Amazon URL
url = 'https://www.amazon.com'
'''
# Opening Amazon.com
driver.get(url)

# Signing in with LoginCredentials

    # Finds the signin prompt
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
time.sleep(x)
    # Finds the username box, Sends username into input box
driver.find_element(By.ID, 'ap_email').send_keys(Username)
time.sleep(x)
    # Clicks continue
driver.find_element(By.ID, 'continue').click()
time.sleep(x)
    # Finds the password box, Sends password into input box
driver.find_element(By.ID, 'ap_password').send_keys(Password)
time.sleep(x)
    # Clicks Submit
driver.find_element(By.ID, 'signInSubmit').click()
time.sleep(x)
'''
# Going to the ASIN store page
url_new = url +'/dp/'+ values[0]
driver.get(url_new)

# Function to find trigger and then

def StockCheck():
    URL_raw = driver.find_element(By.XPATH, '//*[@id="availability"]/span').text
    if URL_raw == 'In Stock.':
        return True
    else:
        time.sleep(3)
        driver.refresh()
        return StockCheck()
if StockCheck() != True:
    sys.exit()
else:None

# If trigger is found and is true

    # Finds Add to Cart button, clicks
driver.find_element(By.ID, 'add-to-cart-button').click()

print('Item ', values, ' has been added to cart.')

