try:
	d=[1,2,3,4]
	
	print(d)
	print(d[5])
	raise NameError
	raise TypeError

except TypeError:
	print("your number is out of range")
except  IndexError:
	print("index is out of range")
finally:
	print("execution complied")
