# AmazonBot
A repository  for my amazon bot

Read the instructions please!

# UPDATE 1
Added scalability so that a reasonable number of ASIN numbers can be added into ItemInfo.json. Also debugged the directory issues in ItemInfo.py and LoginCredentials.py.

# UPDATE 2
Replaced a bunch of inefficient code. Such as 'string' + 'string' changed to f'string{string}'. Created a central dictionary for item info which now includes price values to allow for price checking. Bot now closes when item is added to cart or other specific action is done. Changed all 'n' values to independent named variables for readability. Added a price check function, which works sometimes but not all the time still have some testing to do on it.

# Upcoming UPDATES
Fix price check is at the top of my list. Also I plan on minimizing the total amount of files that are in this repository to below 4. Having so many files seems redundant and inefficient.
