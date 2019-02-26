import random
l=["r","p","s"]
while True:
	#form user
	u=input("enter your choice,press n to discontinue" )
	if u=='n':
		print("game over")
		exit()
		#form comp
	c=random.choice(l)
	print("computer choice",c)
	#compare user and comp
	if u==c:
		print("tie")
	elif u=="r" and c=="p":
		print("comp wins")
	elif u=="r" and c=="s":
		print("you win")
	elif u=="p" and c=="r":
		print("you win" )
	elif u=="p" and c=="s":
		print("comp wins")
	elif u=="s" and c=="p":
		print("you win")
	elif u=="s" and c=="r":
		print("comp wins")
			


	    	




