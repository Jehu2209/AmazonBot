# Copyright 2021, Jehu Morning, All rights reserved.

# Turning the values into urls

# Importing the ASIN list from ItemInfo.py
from BotFiles.ItemInfo import ASIN_values

# Empty List
URL_list = []

# Function for turning adding the values to a base url
def URLCreator(values, emptyList):
    url_base = 'https://www.amazon.com/dp'
    base_int = 0
    for i in values:
        emptyList.append(url_base + '/' + values[base_int])
        base_int += 1

# Calling the function and appendin url_list with the ASIN values
URLCreator(ASIN_values, URL_list)