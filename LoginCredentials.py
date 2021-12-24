# Converting information in JSON to sendable keys

# Module imports
import json
import os

# Path to the json
json_path = os.getcwd()

# Opening the JSON
data = open(json_path + '\\LoginCredentials.json')
json_data = json.load(data)

# Storing the json data into variables TODO : Replace personal info from LoginCredentials.json with place holds
Username = json_data['Login_Credentials']['UserEmail']
Password = json_data['Login_Credentials']['Password']
