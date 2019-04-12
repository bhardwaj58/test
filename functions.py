def new(x=0,y=0):

	print("Welcome to the new programme")
	print("What would you like to do with this programme, choose from below options")
	operation =input("Addition, Multiplication, Subtraction, Division: ")
	x = int(input("enter the first number: "))
	y = int(input("enter the second number: "))
	if operation.upper()[0] is "A":
		print(x+y)
	elif operation.upper()[0] is "M":
		print(x*y)

	elif operation.upper()[0] is "S":
		print(x-y)

	elif operation.upper()[0] is "D":
		print(x/y)
	else:
		print("please select the correct option")
new()
