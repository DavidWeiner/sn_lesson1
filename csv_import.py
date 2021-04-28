with open("list.csv", "r") as lista:
    contents = lista.read().splitlines()
    for sorok in contents:
        row_data = sorok.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}")
    # print(contents)
    # print(row_data[0])
