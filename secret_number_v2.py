import random
n = random.randint(1 , 5)
guess = int(input("Enter your number, between 1-5\n"))
#print(n)
#miert nem irja ki amikor kitalaltam, ezt meg ki kell nyomozni?
#ciklusnak utana kell nezni
while n != guess:
    if n == guess:
        print("you guessed it!")
    else:
        print("wrong number")
        guess = int(input("Enter your number, between 1-5\n"))