secret = 25
guess = input("Enter your number, between 1-30\n")
guess =int(guess)

if secret == guess:
    print("you're lucky")
else:
    print("try again")
