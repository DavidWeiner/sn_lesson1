guess = int(input("choose a number (between 1 and 100): "))
for i in range(1, guess+1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} fizzbuzz")
    elif i % 3 == 0:
        print(f"{i} fizz")
    elif i % 5 == 0:
        print(f"{i} buzz")
    else:
        print(i)