print("this program convert km to miles")
repeat = "n"

while True:
    km = int(input("please enter the km\n"))
    miles = km * 0.621371
    print(f"{km}km is equal to {miles}mile(s)")
    answer = input("would you like to do another convert? please type y/n \n")
# hogy lehet levagni a tizedes pontot, mondjuk .2 tizedesjegyig
    if answer != "y":
        print("ok, bye")
        break
