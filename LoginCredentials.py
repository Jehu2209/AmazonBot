# Converting information in JSON to sendable keys in bot

# Module imports
import json

# Path to the json
json_path = 'AmazonBot_Test\\JsonFiles\\LoginCredentials.json'

# Opening the JSON
data = open(json_path)
json_data = json.load(data)

# Putting the json data into variables
Username = json_data['Login_Credentials']['Username']
Password = json_data['Login_Credentials']['Password']


