# AmazonBot
A repository for my amazon bot. Use of this bot in accordance with Amazon.com TOS.

# About the bot:
This bot is really my first major project with python which I have used to really learn how to program, while its not perfect it works well with minimum bugs and does its task.

# How to use:
1. Make sure you are using python 3 not python 2.7
2. Clone this repository to your files and make sure to write down the path to the file i.e.(/usr/path/to/file)
3. [Install pip to your computer](https://pip.pypa.io/en/stable/installation/)
4. pip install the following modules to the previous file path:
  ```python
  $ cd /usr/path/to/file
  pip install selenium
  pip install webdriver-manager
  pip install requests
  pip install bs4
  ```
5. Open up BotBuildInfo.json
6. Go to "UserEmail": and replace "email" with your amazon email.
7. Go to "UserPassword": and replace "password" with your amazon password.
!!Remember that these files are not encrypted, so please make sure that your device is secure before putting in sensitive info such as your amazon username and password. These files are saved as plain text so anyone who has access to your computer can read them.!!
8. Go to Item_1 and replace the "ASIN_NUMBER" value with the item you want the bot to buy ([What is an ASIN](https://www.nchannel.com/blog/amazon-asin-what-is-an-asin-number/)). Then replace both "MIN_PRICE" and "MAX_PRICE" with the minimum price and maximum price you want to pay. It is important to note that minimum price should not be placed at 0, due to the chance the bot will buy a fake item.
9. Repeat step 8 with Item_2 -> Item_N for as many items you want. Simply copy the entire bracket, then paste below the last item and remove the comma at the end of the bracket
Example ->
```json
"Item_1": {
  "ASIN_NUMBER": "B08W8DGK3X",
  "MIN_PRICE": 199,
  "MAX_PRICE": 499
  },
"Item_N": {
  "ASIN_NUMBER": "item_n_asin",
  "MIN_PRICE": "item_n_min_price",
  "MAX_PRICE": "item_n_max_price"
  }
```
10. Now the bot is ready to run, open up terminal and enter the following code:
```cmd
python /user/path/to/BotBuild.py
```

  
