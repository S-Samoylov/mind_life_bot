import requests as req
from requests.exceptions import HTTPError
import sys
import time
import json

print("Pls, enter your bot token")
token = input()
url = f"https://api.telegram.org/bot{token}"

response = req.get(url + "/getMe")
if (response.status_code != 200):
	f = open("log.txt", "a")
	f.write(time.asctime() + "            getMe " + url + "/getMe\n")
	f.close()
	print("Fucking getme error")
	sys.exit()
	
while (True):
	response = req.get(url + "/getUpdates")
	resp_js = json.loads(response.text)
	for message in reversed(resp_js["result"]):
		s = message["message"]["text"]
		if (s[0] == "/"):
			if (s == "/start"):
				#start bot
				print("Bot answering")
				mess = "Hello, guy"
				params = {'chat_id': message["message"]["chat"]["id"], 'text': mess}
				req.get(url + "/sendMessage", params = params)
				sys.exit()
			elif (s == "/suck"):
				mess = "Your mom has done it"
				params = {'chat_id': message["message"]["chat"]["id"], 'text': mess}
				req.get(url + "/sendMessage", params = params)
				sys.exit()
			else:
				pass
		else:
			pass
		
	