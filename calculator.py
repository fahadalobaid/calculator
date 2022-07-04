

def calculator (num1,num2,operation):
	print(operation)
	if operation == "+":
		return num1 + num2
	elif operation == "-":
		return  num1 - num2
	elif operation == "*":
		return num1 * num2
	elif operation == "/":
		return  num1 / num2
	else:
		return None
		 
	


def main():

	num1 = input("Enter the first number:")
	num2 = input("Enter the second number:")
	if num1.isdigit() and num2.isdigit():
		operation = input("Choose the operation (+, -, /, *):")
		if operation == "+" or operation == "-" or operation =="*" or operation == "/":
			
			answer = calculator(int(num1),int(num2),operation)
			print("the answer is:"+ str(answer))
		else:
			print("the operation is not valid")
		
	
	else:
		print("the input is not number")
		
			


if __name__ == '__main__':
	main()
