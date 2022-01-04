# AmazonBot
A repository  for my amazon bot

# UPDATE 1
Added scalability so that a reasonable number of ASIN numbers can be added into ItemInfo.json. Also debugged the directory issues in ItemInfo.py and LoginCredentials.py.

# UPDATE 2
Replaced a bunch of inefficient code. Such as 'string' + 'string' changed to f'string{string}'. Created a central dictionary for item info which now includes price values to allow for price checking. Bot now closes when item is added to cart or other specific action is done. Changed all 'n' values to independent named variables for readability. Added a price check function, which works sometimes but not all the time still have some testing to do on it.

# UPDATE 3
The big one! So to begin this I first converted the previous files, Bot_Build.py, ItemInfo.py, LoginCredentials.py, and URLCreation.py to a single 'mega' file BotBuild.py. I added the PriceCheck() function which implements BeautifulSoup webscraping functions to grab and format the specified items price, and checks that the price is between a minimum price parameter and a maximum price parameter. Next I rebuilt ProductCheck() function, reducing the number of lines from 21 to 14 while implementing PriceCheck() function as a parameter for the item to be added to cart. Finally, I structured a dictionary that holds all the item and user information for the bot to use in both sign in and ProductCheck().

# Upcoming UPDATES
As of now I am considering this project complete. There probably won't be anymore major updates, except if I start messing around with the system Recursion. There will be minor updates for readability and testing but everything works now!
