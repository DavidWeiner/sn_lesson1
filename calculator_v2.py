import operator
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
operation = input("What do you want: + - * / \n")
action = {
    "+" : operator.add,
    "-" : operator.sub,
    "/" : operator.truediv,
    "*" : operator.mul,
}
print(action[operation](number1, number2))