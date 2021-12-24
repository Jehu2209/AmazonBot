# Converting information in JSON to sendable keys in bot

# Module imports
import json
import os

# Path to the json
json_path = os.getcwd()

# Opening the JSON
data = open(json_path + '\\ItemInfo.json')
json_data = json.load(data)

# Storing the json data into a list
Items = json_data['ItemNumbers']['Items'].items()
ASIN_values = []
for items in Items:
    ASIN_values.append(items[1])
