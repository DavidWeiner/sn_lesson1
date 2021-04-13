
mood = input("""What is your mood today? Choose from a list 
            1 - happy 
            2 - nervous
            3 - sad
            4 - excited
            5 - relaxed\n """)
#melyik a szebb megoldas a szoveg toresre?
#mood = input("What is your mood today? Choose from a list\n 1 - happy \n 2 - nervous\n 3 - sad\n 4 - excited\n 5 - relaxed\n" )
mood = int(mood)

if mood == 1:
    print("It is great to see you happy!")
elif mood == 2:
    print("Take a deep breath 3 times.")
elif mood == 3:
    print("Don't be sad, the sun is shining.")
elif mood == 4:
    print("Why? Did you win the lottery?")
elif mood == 5:
    print("Good for you!")
else:
    print("I don't recognize this mood")