import random
n = random.randint(1 , 5)
guess = 0
#guess = int(input("Enter your number, between 1-5\n"))
#print(n)
#miert nem irja ki amikor kitalaltam, ezt meg ki kell nyomozni?
#ciklusnak utana kell nezni
while n != guess:
    guess = int(input("Enter your number, between 1-5\n"))
    if n == guess:
        print(f"you guessed it! the correct number is {n}")
    else:
        print("wrong number")