#txt = input("Please type your text here: ")
#print(txt.lower())
#print(txt.upper())

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
