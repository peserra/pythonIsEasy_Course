ROW_NUMBER = 6
COLUMN_NUMBER = 7
player = 1
game = True
currField = [[" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "]]

rowSpotsCounter = [5, 5, 5, 5, 5, 5, 5]


def drawField(row, col, field):
    rows = int(row+(row-1))  # 6 + 5 = 11 = 0-10 indice
    columns = int(col+(col-1))  # 7+6 = 13 = 0-12 indice

    for row in range(rows):
        if row % 2 == 0:  # if its a even row
            # converts the row to match the index in our matrix (had to be an integer)
            practicalRow = int(row/2)
            for column in range(columns):
                if column % 2 == 0:
                    # converts the column to match the index in our matrix (it had to be an integer)
                    practicalColumn = int(column/2)
                    if column != columns-1:
                        # will print the symbol of the matrix here, corresponding to the index of the board
                        print(field[practicalRow][practicalColumn], end="")
                    else:
                        # prints the last symbol of the row
                        print(field[practicalRow][practicalColumn])
                else:
                    print("|", end="")
        else:
            print("-"*columns)


def checkWinner(field, rowCount, colCount, player):
    if player == 1:
        piece = "X"
    else:
        piece = "O"
    # Horizontal
    for row in range(rowCount):
        for col in range(colCount-3):
            if field[row][col] == piece and field[row][col+1] == piece and field[row][col+2] == piece and field[row][col+3] == piece:
                print(f"The winner is Player {player}! Congrats!!")
                return True
    # Vertical
    for row in range(rowCount-3):
        for col in range(colCount):
            if field[row][col] == piece and field[row+1][col] == piece and field[row+2][col] == piece and field[row+3][col] == piece:
                print(f"The winner is Player {player}! Congrats!!")
                return True
    # Diagonal 1
    for row in range(rowCount-3):
        for col in range(colCount-3):
            if field[row][col] == piece and field[row+1][col+1] == piece and field[row+2][col+2] == piece and field[row+3][col+3] == piece:
                print(f"The winner is Player {player}! Congrats!!")
                return True
    # Diagonal 2
    for row in range(3, rowCount):
        for col in range(colCount-3):
            if field[row][col] == piece and field[row-1][col+1] == piece and field[row-2][col+2] == piece and field[row-3][col+3] == piece:
                print(f"The winner is Player {player}! Congrats!!")
                return True
    return False


def gameMovement(column, player, rowCounter, field):
    if field[rowCounter[column]][column] == " " and player == 1:
        field[rowCounter[column]][column] = "X"
    if field[rowCounter[column]][column] == " " and player == 2:
        field[rowCounter[column]][column] = "O"
    rowCounter[column] -= 1


while(game):
    print(f"Player {player} Turn!")
    moveCol = (int(input("Enter the column number (1-7): "))-1)
    if player == 1:
        gameMovement(moveCol, player, rowSpotsCounter, currField)
        drawField(ROW_NUMBER, COLUMN_NUMBER, currField)
        winner = checkWinner(currField, ROW_NUMBER, COLUMN_NUMBER, player)
        print(rowSpotsCounter[moveCol])
        if winner is True:
            game = False
        player = 2
    else:
        gameMovement(moveCol, player, rowSpotsCounter, currField)
        drawField(ROW_NUMBER, COLUMN_NUMBER, currField)
        winner = checkWinner(currField, ROW_NUMBER, COLUMN_NUMBER, player)
        print(rowSpotsCounter[moveCol])
        if winner is True:
            game = False
        player = 1
