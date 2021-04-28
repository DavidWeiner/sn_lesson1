dict = {}

while True:
    menu = int(input("Choose an option: \n" + " 1 - new contact \n" + " 2 - search contact \n" + " 3 - exit \n"))

    if menu == 1:
        username = str(input("Please add a name: \n"))
        phonenum = str(input("Please add the number \n"))
        dict.update({username:phonenum})
        print(dict)

    elif menu == 2:   # hogy lehet toredek nevre keresni?
        scontact = str(input("What do you search? \n"))
        if scontact in dict.keys():
            print("Name: ", scontact, " and ", "Number: ", dict[scontact])
        else:
            print("There is no information")

    elif menu == 3:
        print("Ok, bye")
        break