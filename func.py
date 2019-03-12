#creating a function
def func1():
	print("hi")

func1()
#with parameter
def func2(a):
	print("hi"+a)
func2("harshita")
#with 2 parameter
def func3(a,b):
	c=a+b
	print(c)
func3(2,7)
#with default parameter
def func4(university ="IIBT"):
	print("i am in"+'\t'+university)

func4("IITB")
func4("IITR")
func4()
#calling one function from other
def func5():
	print("hi other function")
def func6():
	print("hello ,I am going to call other function")
	func5()
func6()
#using parameter
def func5(a,b):
	print("hi other function")
	c=a+b
	print(c)


def func6():
	print("hello ,I am going to call other function")
	func5(2,7)
func6()
#return data
def func5(a,b):
	print("hi other function")
	c=a+b
	return(c)


def func6():
	print("hello ,I am going to call other function")
	s=func5(2,7)
	print("addition is",s)
func6()



