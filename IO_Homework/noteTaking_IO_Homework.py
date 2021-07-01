# when the program startsUp we should put a filename
usedNames = []
while (True):
    # if the file does not exist, it should let the user to write the text in the file, after this should save and exit the file
    fileName = input("Please insert the file name: ")
    if fileName == "EXIT":
        break
    elif fileName not in usedNames:
        with open(f"{fileName}.txt", "w") as noteTaking:
            s = input()
            noteTaking.write(s)
            usedNames.append(fileName)
# if the file already exists it should give options read the file [read], delete and start over[write], append the file [append]
    else:
        print("The file with that name already exists! Please choose an action!")
        action = input(
            "type 'r' to read the file, 'w' to delete and start a new file, 'a' to append to the file and 'c' to change a line: ")

        if action == "r":
            with open(f"{fileName}.txt", "r") as noteTaking:
                print(noteTaking.read())

        elif action == "w":
            with open(f"{fileName}.txt", "w") as noteTaking:
                s = input()
                noteTaking.write(s)

        elif action == "a":
            with open(f"{fileName}.txt", "a") as noteTaking:
                s = input()
                noteTaking.write(s)

        else:
            break

    print(usedNames)
