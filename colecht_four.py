print("Welcome! Did you know Captain James Cook played this game on long voyages?")
print("Enjoy Crabbing with Cook!!")

def row_setup(row_and_column_max, row_and_column_min):
    """
    input: row and column max and min
    usage: user selects dimensions of game within limits
    output: number of rows
    """
    try:
        rows = int(input("How deep is your ocean? Please enter a number ({}-{}, 6 is standard) > ".format(row_and_column_min, row_and_column_max)))
    except ValueError:
        rows = int(input("How deep is your ocean? Please enter a valid number ({}-{}, 6 is standard) > ".format(row_and_column_min, row_and_column_max)))
    while rows < row_and_column_min or rows > row_and_column_max:
        print("That is not a valid input.")
        rows = int(input("How deep is your ocean? Please enter a number ({}-{}, 6 is standard) > ".format(row_and_column_min, row_and_column_max)))
    return rows

def column_setup(row_and_column_max, row_and_column_min):
    """
    input: row and column max and min
    usage: user selects dimensions of game within limits
    output: number of columns
    """
    try:
        columns = int(input("How wide is your ocean? Please enter a number ({}-{}, 7 is standard) > ".format(row_and_column_min, row_and_column_max)))
    except ValueError:
        columns = int(input("How wide is your ocean? Please enter a valid number ({}-{}, 7 is standard) > ".format(row_and_column_min, row_and_column_max)))
    while columns < row_and_column_min or columns > row_and_column_max:
        print("That is not a valid input.")
        columns = int(input("How wide is your ocean? Please enter a number ({}-{}, 7 is standard) > ".format(row_and_column_min, row_and_column_max)))
    return columns

def create_board(rows, columns):
    """
    input: integer for rows and columns
    usage: create board list of lists using user-entered #s for rows and columns
    output: is a populated blank board list of lists
    """
    board = []
    for i in range(0,rows):
        board.append([])
        for j in range(0,columns):
            board[i].append("*")
    return board

def print_board(board):
    """
    input: board list of lists
    usage: print current status of board
    output: none, prints only
    """
    for row in board:
        print(" ".join(row))

def column_select(rows, columns, board, current_turn):
    """
    input: rows and columns as integers, board as list of lists, current_turn
    usage: take column selection, check if space is open, change value
    output: new board list of lists
    """
    try:
        column_selection = int(input("Player {}, please choose a column > ".format(current_turn)))
    except ValueError:
        column_selection = int(input("Player {}, please choose a valid column > ".format(current_turn)))
    while column_selection < 0 or column_selection > columns - 1 or board[0][column_selection] != "*":
        column_selection = int(input("Player {}, please choose a valid column > ".format(current_turn)))
    for i in range(rows-1,-1,-1):
        if board[i][column_selection] == "*":
            board[i][column_selection] = current_turn
            break
    return board

def is_horizontal_win(rows, columns, board):
    """
    input: rows and columns as integers, board as list of lists
    usage: check all XXX possible winning combinations
    output: True if win state accomplished, otherwise False
    """
    for h in range(0, rows):
        for c in range(0, columns - 3):
            if board[h][c] == board[h][c + 1] == board[h][c + 2] == board[h][c + 3] != "*":
                return True

def is_vertical_win(rows, columns, board):
    """
    input: rows and columns as integers, board as list of lists
    usage: check all XXX possible winning combinations
    output: True if win state accomplished, otherwise False
    """
    for v in range(0, rows - 3):
        for c in range(0, columns):
            if board[v][c] == board[v + 1][c] == board[v + 2][c] == board[v + 3][c] != "*":
                return True

def is_diagonal_up_win(rows, columns, board):
    """
    input: rows and columns as integers, board as list of lists
    usage: check all XXX possible winning combinations
    output: True if win state accomplished, otherwise False
    """
    for du in range(3, rows):
        for c in range(0, columns - 3):
            if board[du][c] == board[du - 1][c + 1] == board[du - 2][c + 2] == board[du - 3][c + 3] != "*":
                return True

def is_diagonal_down_win(rows, columns, board):
    """
    input: rows and columns as integers, board as list of lists
    usage: check all XXX possible winning combinations
    output: True if win state accomplished, otherwise False
    """
    for dd in range(0, rows - 3):
        for c in range(0, columns - 3):
            if board[dd][c] == board[dd + 1][c + 1] == board[dd + 2][c + 2] == board[dd + 3][c + 3] != "*":
                return True

def is_win(rows, columns, board):
    """
    input: rows and columns as integers, board as list of lists
    usage: check all possible winning combinations
    output: False if win state accomplished, otherwise True
    """
    winning = "no"
    if is_vertical_win(rows, columns, board) or \
       is_horizontal_win(rows, columns, board) or \
       is_diagonal_up_win(rows, columns, board) or \
       is_diagonal_down_win(rows, columns, board):
        winning = "yes"
    if winning == "yes":
        return False
    else:
        return True

def change_turns(current_turn):
    """
    input: current_turn
    usage: change turns
    output: current_turn
    """
    if current_turn == "O":
        current_turn = "X"
    else:
        current_turn = "O"
    return current_turn

def app():
    """
    input: none
    usage: calls all necessary functions to play two player connect four
    output: no output, prints current status of game after every turn
    """
    row_and_column_max = 10
    row_and_column_min = 4
    current_turn = "O"
    current_turn = change_turns(current_turn)
    rows = row_setup(row_and_column_max, row_and_column_min)
    columns = column_setup(row_and_column_max, row_and_column_min)
    board = create_board(rows, columns)
    print_board(board)
    board = column_select(rows, columns, board, current_turn)
    while is_win(rows, columns, board):
        print_board(board)
        current_turn = change_turns(current_turn)
        board = column_select(rows, columns, board, current_turn)
        if sum(x.count("*") for x in board) == 0: # if no free spaces, break
            break
    if is_win(rows, columns, board) == True: # game ends with no winner
        print("It is a tie! Thanks for playing.")
    else:
        print("Congratulations Player {}, you win!".format(current_turn))
    print_board(board)

app()
