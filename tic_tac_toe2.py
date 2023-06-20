# Tic Tac Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if any player has won
def check_win(player):
    # Check rows
    if board[0] == board[1] == board[2] == player or \
       board[3] == board[4] == board[5] == player or \
       board[6] == board[7] == board[8] == player:
        return True
    # Check columns
    if board[0] == board[3] == board[6] == player or \
       board[1] == board[4] == board[7] == player or \
       board[2] == board[5] == board[8] == player:
        return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player or \
       board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Main game loop
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()
        position = int(input("Enter a position (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = current_player

            if check_win(current_player):
                display_board()
                print("Player", current_player, "wins!")
                game_over = True
            elif is_board_full():
                display_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already filled. Try again.")