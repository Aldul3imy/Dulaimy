x=10000000
while x < 99999999:
	print(x)
	f = open("demo.txt", "a")
	f.write(str(x)+"\n")
	x=x+1
	