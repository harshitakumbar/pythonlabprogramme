import random
l=["r","p","s"]
us=0
cs=0
while True:
	#form user
	u=input("enter your choice,press n to discontinue" )
	print("user choice",u)
	d={'r':'rock','p':'papper','s':'scissor'}
	if u in d:
		print(u,d[u])

	if u=='n':
		print("game over")
		print(us,cs)	
		print("user score",us)
		print("comp score",cs)
		if us>cs:
			print("user wins" )
		elif cs>us:
			print("comp wins")
		else:
			print("tie")
		exit()
		#form comp
	c=random.choice(l)
	print("computer choice",c)
	if u in d:
		print(u,d[u])

	#compare user and comp
	if u==c:
		print("tie")
	elif u=="r" and c=="p":
		print("comp wins")
		cs=cs+1
	elif u=="r" and c=="s":
		print("you win")
		us=us=1
	elif u=="p" and c=="r":
		print("you win" )
		us=us=1
	elif u=="p" and c=="s":
		print("comp wins")
		cs=cs+1
	elif u=="s" and c=="p":
		print("you win")
		us=us=1
	elif u=="s" and c=="r":
		print("comp wins")
		cs=cs+1
			


	    	




