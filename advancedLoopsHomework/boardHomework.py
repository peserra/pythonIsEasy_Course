
def board(rows, columns):  # number of spaces of the rows, number of blank lines of the rows
    if rows > 24 or columns > 119:  # max value of my monitor
        return False
    else:
        rows = int(rows + (rows - 1))  # convert into a sequencial row
        # convert into a sequencial column
        columns = int(columns + (columns-1))

        for row in range(rows):
            if row % 2 == 0:
                for column in range(1, columns+1):
                    if column % 2 == 1:
                        if column != (columns):
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        return True


# board(24, 120) False
# board(25, 119) False
board(3, 3) 
