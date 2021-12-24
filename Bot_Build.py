# Utlizing Selenium to construct the bot

# Importing variables TODO : Test whether importing from seperate .py files becomes a problem
from BotFiles.LoginCredentials import Username, Password
from BotFiles.ItemInfo import ASIN_values
from BotFiles.URL_Creation import URL_list

# Importing modules TODO : Determine which modules are unneeded
    # Selenium modules for bot automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
    # System modules for various uses
import os
import time
import sys

# Used in ProductCheck() to pause the function to increase time before stack overflow
wait_time = int(input('Input wait time between repetitions(3 seconds is recommended):'))

# Path to Chrome Driver
driver_path = os.getcwd() + '\\ChromeDriver\\chromedriver.exe'
ser_path = Service(driver_path)

# Creates an instance of webdriver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_path, options=chrome_options)

# Determines whether Bot runs headless
    # Receiving input either yes or no
headless_run = str(input('Run headless? y/n:'))
    # Testing input
if headless_run == 'y':
    # If yes runs bot headless
    chrome_options.add_argument("--headless")
else:True

# Amazon URL
amazon_url = 'https://www.amazon.com'

# Opening Amazon.com
driver.get(amazon_url)

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
def StockCheck(): # TODO : Create and test a solely stock checking feature
    availability_text = driver.find_element(By.XPATH, '//*[@id="availability"]/span').text
    if availability_text == 'Out of Stock.': # TODO : Change this to 'In Stock.' when finished testing
        return True
    else:
        return False

# Function which takes the product availability and cycles through until StockCheck() returns True
def ProductCheck():
    n = 0 # TODO : Consider changing all instances of 'n' to different variables to avoid errors
    ListItems = len(URL_list) - 1 # Gets the number of items in the URL_List
    while n <= ListItems: # Cycles through URL_list, opening, testing, and closing each url in loop
        driver.get(URL_list[n])
        time.sleep(wait_time) # Waits before starting calling StockCheck()
        if StockCheck() == True: # StockCheck() finds the availability of the item by scraping the html
            # TODO : Change on release to 'Buy Now'- (id="buy-now-button")
            driver.find_element(By.ID, 'add-to-cart-button').click() # Finds and clicks the Add to Cart buttom
        else: n += 1
    if n > (ListItems - 1): n = 0 # Resets n after the last item in URL_list has been checked
    return ProductCheck()

# Calling the function
ProductCheck()
