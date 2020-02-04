import sys
def main():
	num1=input("Enter your first number: ")
	num2=input("Enter your second number: ")
	char=input("Choose the operation: ")

	if num1.isdigit()==False or num2.isdigit()==False:
		print("only numbers please")
		

	if num1.isdigit()==True and num2.isdigit()==True and char=='*':
			num1=int(num1)
			num2=int(num2)
			print (num1*num2)
	elif num1.isdigit()==True and num2.isdigit()==True and char=='+':
			num1=int(num1)
			num2=int(num2)
			print (num1+num2)
	elif num1.isdigit()==True and num2.isdigit()==True and char=='-':
			num1=int(num1)
			num2=int(num2)
			print (num1-num2)
	elif num1.isdigit()==True and num2.isdigit()==True and char=='/':
			num1=int(num1)
			num2=int(num2)
			print (num1/num2)

	pass




if __name__ == '__main__':
	main()
