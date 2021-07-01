# to do this, first we have to draw our board (we can use our program to do this):
''' Indexes example:
0 0|2|4   
1 -----
2  | |
3 -----
4  | |  '''

# printing the board


def drawField(field):  # field is the matrix that have tha symbols organized
    for row in range(5):
        if row % 2 == 0:  # if its a even row
            # converts the row to match the index in our matrix (had to be an integer)
            practicalRow = int(row/2)
            for column in range(5):
                if column % 2 == 0:
                    # converts the column to match the index in our matrix (it had to be an integer)
                    practicalColumn = int(column/2)
                    if column != 4:
                        # will print the symbol of the matrix here, corresponding to the index of the board
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        # prints the last symbol of the row
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
        else:
            print("-----")

# function to check a winner or a tie


def checkWinner(field, available):
    for i in range(3):
        # horizontal
        if field[0][i] == field[1][i] and field[1][i] == field[2][i] and field[0][i] != " ":
            print(f"The winner is {field[0][i]} player!")
            return True
        # vertical
        elif field[i][0] == field[i][1] and field[i][1] == field[i][2] and field[i][0] != " ":
            print(f"The winner is {field[i][0]} player!")
            return True
        # Principal diagonal
        elif field[0][0] == field[1][1] and field[1][1] == field[2][2] and field[0][0] != " ":
            print(f"The winner is {field[0][0]} player!")
            return True
        # Secondary Diagonal
        elif field[2][0] == field[1][1] and field[1][1] == field[0][2] and field[2][0] != " ":
            print(f"The winner is {field[0][0]} player!")
            return True
        elif not available:  # a tie is considered when the board is full and we have no winner
            print("Its a Tie :(")
            return True
    return False


# a game needs to know wich player is playing at the moment
player = 1

# and a place to register our comands
# the symbols will be registered inside the matrix
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

availablePos = []  # list to check if board have space
for i in range(3):
    for j in range(3):
        availablePos.append(currentField[i][j])  # fill the board with space

drawField(currentField)

# To do a game, we can put our comands inside a eternal loop
while(True):
    print(f"Player {player} Turn!")
    # player row coordinate
    moveRow = int(input("Enter the row number (0-2): "))
    # player column coordinate
    moveCol = int(input("Enter the column number (0-2): "))

    # turns
    if player == 1:
        if currentField[moveCol][moveRow] == " ":
            # player one marks X in the coordinates if there are no marks yet
            currentField[moveCol][moveRow] = "X"
            # draw field before new turn to check the game
            drawField(currentField)
            availablePos.pop()  # each turn we remove one available position of the board
            # function to verify winner
            winner = checkWinner(currentField, availablePos)
            if winner is True:  # verify if we have a winner to break the loop
                break
            player = 2  # change turn
        else:
            # if we try to mark an already marked position on the board
            print("Invalid move, please try again")
            player = 1

    else:
        if currentField[moveCol][moveRow] == " ":
            currentField[moveCol][moveRow] = "O"
            drawField(currentField)
            availablePos.pop()
            winner = checkWinner(currentField, availablePos)
            if winner is True:
                break
            player = 1
        else:
            print("Invalid move, please try again")
            player = 2
