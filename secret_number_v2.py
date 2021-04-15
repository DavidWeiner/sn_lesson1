import random
n = random.randint(1 , 5)
guess = 0

#print(n)
while n != guess:
    guess = int(input("Enter your number, between 1-5\n"))
    if n == guess:
        print(f"you guessed it! the correct number is {n}")
    else:
        print("wrong number")