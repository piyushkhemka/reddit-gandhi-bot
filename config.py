import json

config = json.load(open('config.json'))

username = config['username']
password = config['password']
client_id = config['client_id']
client_secret = config['client_secret']
user_agent = config['user_agent']
