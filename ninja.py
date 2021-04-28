#ninja_file = open("ninja.txt", "r")
with open("ninja.txt", "r") as ninja_file:
    contents = ninja_file.read().splitlines()
    print(contents)

    for line in ninja_file:
        print(line)

with open("ninja2.txt", "w") as ninja_file_2:
    ninja_file_2.write("Hello, new file!")

#ninja_file.close()