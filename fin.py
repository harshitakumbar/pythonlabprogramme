a=int(input("give a number"))
b=int(input("give a number"))
c=int(input("give a number"))
print(a,b,c)
def func1(a,b,c):
	if a>=b and a>=c:
		return a
	elif b>=a and b>=c:
		return b
	elif c>=b and c>=a:
		return c
l=func1(a,b,c)
print(l)
	


