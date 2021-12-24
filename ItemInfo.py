# Converting information in JSON to sendable keys in bot

# Module imports
import json
import os

# Path to the json
json_path = os.getcwd()

# Opening the JSON
data = open(json_path + '\\ItemInfo.json')
json_data = json.load(data)

# Putting the json data into variables
Items = json_data['ItemNumbers']['Items'].items()
values = []
for items in Items:
    values.append(items[1])

