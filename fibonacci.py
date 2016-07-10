import sys
def fibonacci(n):#generator function
	a,b,counter=0,1,0
	while True:
		if(counter <n):
			yield a
			a,b=b,a+b
			counter+=1
		else:
			return
			
f=fibonacci(10)#iterator

while True:
	try:
		print(next(f),end=" ")
	except:
		sys.exit()