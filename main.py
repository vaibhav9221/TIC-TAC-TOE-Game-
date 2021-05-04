# --------- Global Variables -----------

# Lets us know if the game is over yet
game_is_going = True

# Tells us who the current player is (X goes first)
current_player = "X"

# Tells us who the winner is

winner=None

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]





# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():
    Display_board()
    while game_is_going:

         # Handle a turn
        handle_turn(current_player)
        
        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_palyer()

    # Since the game is over, print the winner or tie
    if winner == "X" or winner == "O":
        print("*************       "+winner+"     won!***********")

    else:
        print("*********MATCH TIE **********")

# Display the game board to the screen
def Display_board():
    print(board[0]+" | "+board[1]+" | "+board[2]+" | ")
    print(board[3]+" | "+board[4]+" | "+board[5]+" | ")
    print(board[6]+" | "+board[7]+" | "+board[8]+" | ")

# Handle a turn for an arbitrary player
def handle_turn(player):
    
    print(player+" = TURN !")
    # position = input(" Choose position between 1 to 9 :")
    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid=True
    while valid:
        position = input(" Choose position between 1 to 9 ")
        
        # Make sure the input is valid
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input(" Choose position between 1 to 9 ")
        
        # Get correct index in our board list
        position = int(position)-1
        
        # Then also make sure the spot is available on the board
        
        if board[position] !="-":
            print("You Can't go there :")
        else:
            valid=False

    # Put the game piece on the board
    board[position] = player

    # Show the game board
    Display_board()


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    
    check_if_tie()

# Check to see if somebody has won
def check_for_winner():
    # Set global variables
    global winner 
    # Check if there was a winner anywhere
    #check rows
    row_winner=check_row()

    #check column
    column_winner=check_column()

    #check diagonal
    diagonal_winner=check_diagonals()
    
    # Get the winner
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None

# Check the rows for a win
def check_row():

    # Set global variables
    global game_is_going

    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0]==board[1]==board[2] !="-"
    row_2 = board[3]==board[4]==board[5] !="-"
    row_3 = board[6]==board[7]==board[8] !="-"
    
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_is_going=False
    
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

# Check the columns for a win
def check_column():

    # Set global variables
    global game_is_going

    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0]==board[3]==board[6] !="-"
    column_2 = board[1]==board[4]==board[7] !="-"
    column_3 = board[2]==board[5]==board[8] !="-"

    # If any colimns does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_is_going=False

    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

# Check the diagonals for a win
def check_diagonals():

    # Set global variables
    global game_is_going

     # Check if any of the diagonals have all the same value (and is not empty)
    diagonal_1 = board[0]==board[4]==board[8] !="-"
    diagonal_2 = board[6]==board[4]==board[2] !="-"
    
    # If any diagonals does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_is_going=False

    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    
    return

# Check if there is a tie
def check_if_tie():

    # Set global variables
    global game_is_going

    # If board is full
    if "-" not in board:
        game_is_going=False
        return True
    # Else there is no tie
    else:
        return False

# Flip the current player from X to O, or O to X
def flip_palyer():

    # Global variables we need
    global current_player

      # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
      # If the current player was O, make it X
    else:
        current_player = "X"
    


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()
