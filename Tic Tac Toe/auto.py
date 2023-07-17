import random
import time


def display_board(board):
    print("\n" * 100)
    print("\n")
    print("\t     |     |")
    print(f"\t  {board[7]}  |  {board[8]}  | {board[9]} ")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {board[4]}  |  {board[5]}  | {board[6]} ")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {board[1]}  |  {board[2]}  | {board[3]} ")
    print("\t     |     |\n")


def player_input():
    marker = ''

    while marker not in ['X', 'O']:
        marker = input('Player 2, Do you want to be "X" or "O": ').upper()

    if marker == 'X':
        return 'O', 'X'
    else:
        return 'X', 'O'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    winning_combinations = [
        [7, 8, 9], [4, 5, 6], [1, 2, 3],  # horizontal
        [7, 4, 1], [8, 5, 2], [9, 6, 3],  # vertical
        [7, 5, 3], [9, 5, 1]  # diagonal
    ]

    for combination in winning_combinations:
        if all(board[i] == mark for i in combination):
            return True

    return False


def choose_first():
    return random.choice(['Player 1', 'Player 2'])


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return all(space_check(board, i) for i in range(1, 10))


def player_choice(board, player):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        if player == 'Player 1':
            time.sleep(1)
            position = random.randint(1, 9)
        else:
            try:
                position = int(input(f'{player}, choose your next position (1-9): '))
                if not (1 <= position <= 9):
                    print("Invalid input. Please enter a number between 1 and 9.")
                elif not space_check(board, position):
                    print("That position is already taken. Please choose another position.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    return position


def replay():
    return input('Do you want to play again? (yes/no): ').lower().startswith('y')


def play_tic_tac_toe():
    print('Welcome to Tic Tac Toe!')
    print()

    while True:
        Board = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(f'{turn} will go first')

        play_game = input('Are you ready to play the game? Enter "yes" or "no": ')

        if play_game.lower() == 'yes':
            game_on = True
        else:
            game_on = False

        while game_on:
            display_board(Board)
            if turn == 'Player 1':
                position = player_choice(Board, turn)
                place_marker(Board, player1_marker, position)

                if win_check(Board, player1_marker):
                    display_board(Board)
                    print('Congratulations! Player 1 wins the game.')
                    game_on = False
                elif full_board_check(Board):
                    display_board(Board)
                    print('The game is a draw.')
                    break
                else:
                    turn = 'Player 2'
            else:
                position = player_choice(Board, turn)
                place_marker(Board, player2_marker, position)

                if win_check(Board, player2_marker):
                    display_board(Board)
                    print('Congratulations! Player 2 wins the game.')
                    game_on = False
                elif full_board_check(Board):
                    display_board(Board)
                    print('The game is a draw.')
                    break
                else:
                    turn = 'Player 1'

        if not replay():
            break


play_tic_tac_toe()
