#This function compares two numbers and returns them in increasing order. Fill in the blanks, so the print statement displays the result of the function call in order. Hint: if a function returns multiple values, don't forget to store these values in multiple variables

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
num1 = int(input("Enter 1st number to compare:"))
num2 = int(input("Enter 2nd number to compare:"))

smaller, bigger = order_numbers(num1, num2)
print(smaller, bigger)