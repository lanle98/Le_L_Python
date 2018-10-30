def greeting():
	print("Hello from the greeting function");


# the greeting function just says hello
# invoke or call the function
greeting()


def lanle(zzz="batman"):
	print("now we're saying", zzz, "from another function")


lanle()
lanle("something completely different")
lanle("fdhfhdhkfbklfjihfnkdl")

# variables and scope
myNumberVariable = 10


#returning values from functions (very powerful)
def someMath(num1=2,num2=4):
	global myNumberVariable

#
	myNumberVariable = num1 + num2
	return num1 + num2
	print(myNumberVariable)

sum = someMath()
print("we are doing some math and getting", sum)

sum = someMath(10,15)
print("another math operation with", sum, "as the result")



