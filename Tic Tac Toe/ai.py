# Tic-Tac-Toe with AI Player

# Create the game board
board = [' ' for _ in range(9)]


# Function to print the game board
def print_board():
    print('---------')
    for i in range(3):
        print(f'| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]}')
        print('---------')


# Function to check if a player has won
def check_winner(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False


# Function to check if the game is over
def is_game_over():
    return check_winner('X') or check_winner('O') or ' ' not in board


# Function to evaluate the score of a board state
def evaluate():
    if check_winner('X'):
        return 1  # AI wins
    elif check_winner('O'):
        return -1  # Player wins
    else:
        return 0  # Draw


# Minimax algorithm
def minimax(boarded, depth, is_maximizing):
    if check_winner('X'):
        return 1
    elif check_winner('O'):
        return -1
    elif ' ' not in boarded:
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if boarded[i] == ' ':
                boarded[i] = 'X'
                eval_score = minimax(boarded, depth + 1, False)
                boarded[i] = ' '
                max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if boarded[i] == ' ':
                boarded[i] = 'O'
                eval_score = minimax(boarded, depth + 1, True)
                boarded[i] = ' '
                min_eval = min(min_eval, eval_score)
        return min_eval


# Function to make a move for the AI player
def make_ai_move():
    best_eval = float('-inf')
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            eval_score = minimax(board, 0, False)
            board[i] = ' '
            if eval_score > best_eval:
                best_eval = eval_score
                best_move = i
    board[best_move] = 'X'


# Function to play the game
def play_game():
    player = 'O'
    while True:
        print_board()
        if player == 'O':
            move = int(input("Player O, choose your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = player
                if check_winner(player):
                    print_board()
                    print("Player O wins!")
                    break
                elif ' ' not in board:
                    print_board()
                    print("It's a tie!")
                    break
                player = 'X'
            else:
                print("Invalid move. Try again.")
        else:
            make_ai_move()
            if check_winner(player):
                print_board()
                print("Player X wins!")
                break
            elif ' ' not in board:
                print_board()
                print("It's a tie!")
                break
            player = 'O'


# Start the game
play_game()