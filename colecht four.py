import random

# create variables for board (list), rows (int input), and columns (int input)
board = []
current_turn = "X"
winning = "no"

row_and_column_max = 10
row_and_column_min = 4

print("Welcome! Today you are going to play a fun variation of Connect Four...")
print("COLECHT FOUR!")

rows = int(input("Please enter the number of rows you would like ({}-{}, 6 is standard) > ".format(row_and_column_min, row_and_column_max)))
columns = int(input("Please enter the number of columns you would like ({}-{}, 7 is standard) > ".format(row_and_column_min, row_and_column_max)))

# check for rows and columns to ensure they are digits in the acceptable range
while rows < 4 or rows > 10:
    print("That is not a valid input.")
    rows = int(input("Please enter the number of rows you would like ({}-{}, 6 is default) > ".format(row_and_column_min, row_and_column_max)))
    columns = int(input("Please enter the number of columns you would like ({}-{}, 7 is default) > ".format(row_and_column_min, row_and_column_max)))

# initialize board with double for loop
def create_board(rows, columns):
    """
    create board using user-entered #s for rows and columns
    inputs are rows and columns integers from user inputs
    output is a populated board list of lists
    """
    for i in range(0,rows):
        board.append([])
        for j in range(0,columns):
            board[i].append("*")

# printing current status of board
def print_board(board):
    """
    function to print current status of board
    takes a list as an argument, in this case the board list
    output is printing the board list contents with spaces in between
    """
    for row in board:
        print(" ".join(row))

# FUNCTION TO ASK FOR COLUMN SELECTION, CHECK IF OPEN, CHANGE VALUE AS NEEDED
def column_select(rows):
    """
    function to take column selection, check if space is open, and change value
    takes rows as input to cycle through and check for open spaces
    output is to change the value to mark a player's choice
    """
    column_selection = int(input("Player {}, please choose a row > ".format(current_turn)))
    while column_selection < 1 or column_selection > columns:
        column_selection = int(input("Player {}, please choose a valid row > ".format(current_turn)))
    for i in range(0,rows):
        if board[i][column_selection] == "*":
            board[i][column_selection] = current_turn
            break


# ADD IS_WIN(TURN) FUNCTION THAT RETURNS TRUE OR FALSE -- if is false, make next turn
def is_win(current_turn, rows, columns):
    for h in range(0, columns - 3): # horizontal win combinations
        for r in range(0, rows - 3):
            if board[h][r] == board[h][r+1] == board[h][r+2] == board[h][r+3] != "*":
                winning = "yes"
    for v # vertical win combinations

    for du # diagonal-up win combinations

    for dd # diagonal-down win combinations

    if winning = "yes":
        break
    else:
        if current_turn == "X":
            current_turn = "O"
        else:
            current_turn = "X"

# have four separate functions for horizontal, vertical, diagonal-up, and diagonal-down (ending with row/column - 3)

# REPLACE OTHER PARTS OF GAME

# one function to rule, er, run them all
def app():
    """
    function to play tic tac toe with user vs computer selecting at random
    function takes no input but it will prompt the user to enter row and column
    output is printing either the winner or a tie game to the console
    """
    create_board(rows, columns)
    print_board(board)
    column_select()
    is_win(current_turn, rows, columns)

app()

'''
    for i in range(0,9):
        print("It is the {}'s turn.".format(current_turn))
        if current_turn == "o": # computer selection
            row = random.randint(0,2)
            column = random.randint(0,2)
        elif current_turn == "x": # user selection
            row = int(input("Please enter a row number (0-2) > "))
            column = int(input("Please enter a column number (0-2) > "))

        while board[row][column] != "*": # check to make sure spot is open, ask again if necessary
            if current_turn == "o":
                row = random.randint(0,2)
                column = random.randint(0,2)
            elif current_turn == "o":
                print("That spot is already taken.")
                row = int(input("Please enter a row number (0-2) > "))
                column = int(input("Please enter a column number (0-2) > "))

        if current_turn == "o":
            print("The computer chose row {} and column {}.".format(row,column))

        board[row][column] = current_turn # change * to x or o

        for i in range(0,3): # check to see if any winning condition is met
            if board[i][0] == board[i][1] == board[i][2] != "*":
                game_over = "yes"
            elif board[0][i] == board[1][i] == board[2][i] != "*":
                game_over = "yes"
            elif board[0][0] == board[1][1] == board[2][2] != "*":
                game_over = "yes"
            elif board[0][2] == board[1][1] == board[2][0] != "*":
                game_over = "yes"
        if game_over == "yes": # win condition is met, break
            break

        if current_turn == "x": # switch turns
            current_turn = "o"
        else:
            current_turn = "x"

        print_board(board) # print current status of board

    if game_over == "yes":
        print("CONGRATULATIONS to team {}, you win!".format(current_turn))
    else:
        print("Sometimes nobody wins! Game over.")

    print_board(board)

app()
'''
