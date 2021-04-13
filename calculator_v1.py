number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
operation = input("What do you want: + - * / \n")
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("does not recognize this operation")
