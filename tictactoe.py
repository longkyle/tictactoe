#!/usr/bin/env python

"""
Command line version of the classic game, Tic Tac Toe
"""

__author__ = "Kyle Long"
__email__ = "long.kyle@gmail.com"
__date__ = "08/29/2019"
__copyright__ = "Copyright 2019, Kyle Long"
__python_version__ = "3.7.4"


LIGHTGREY = '\033[37m'
END = '\033[0m'

WIN_COMBOS = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 9),
              (1, 4, 7),
              (2, 5, 8),
              (3, 6, 9),
              (3, 5, 7),
              (1, 5, 6))


def main():
    """
    Collects players names.
    Plays game until players quit.
    """
    print('Welcom to Kyle\'s Tic Tac Toe!\n')
    player1 = input('What is Player 1\'s name?: ')
    player2 = input('What is Player 2\'s name?: ')
    print('\n')
    print(f'{player1} will be Xs')
    print(f'{player2} will be Os')
    print('\n')
    print('Good luck to you both!')
    print('\n')
    print('\n')

    while True:
        board = clean_board()
        print_board(board)
        if not play(board, player1, player2):
            print('\nThanks for playing! Goodbye!')
            break

    return


def clean_board():
    """
    Returns a dictionary of data for a clean
    board without any Xs or Os.
    """
    board = {9: f'{LIGHTGREY}9{END}',
             8: f'{LIGHTGREY}8{END}',
             7: f'{LIGHTGREY}7{END}',
             6: f'{LIGHTGREY}6{END}',
             5: f'{LIGHTGREY}5{END}',
             4: f'{LIGHTGREY}4{END}',
             3: f'{LIGHTGREY}3{END}',
             2: f'{LIGHTGREY}2{END}',
             1: f'{LIGHTGREY}1{END}'}

    return board


def print_board(board):
    """
    Prints out a Tic Tac Toe board in it's current state.

    args:
        board (dict):   Holds all X & O info for gameplay
    """

    print()
    print('       |       |       ')
    print(f'   {board[9]}   |   {board[8]}   |   {board[7]}   ')
    print('       |       |       ')
    print('-------+-------+-------')
    print('       |       |       ')
    print(f'   {board[6]}   |   {board[5]}   |   {board[4]}   ')
    print('       |       |       ')
    print('-------+-------+-------')
    print('       |       |       ')
    print(f'   {board[3]}   |   {board[2]}   |   {board[1]}   ')
    print('       |       |       ')
    print()

    return


def play(board, player1, player2):
    """
    Indicates when it is each players turn.
    Reprints the board & checks for a winner after each turn.
    Checks if players want to play again upon completion of each game.

    args:
        board (dict):   Holds all X & O info for gameplay
        player1 (str):  player1's name
        player2 (str):  player2's name
    """
    for i in range(1, 10):
        # player1's turn
        if i % 2 == 1:
            p = player1
            marker = 'X'
        # player2's turn
        else:
            p = player2
            marker = 'O'

        while True:
            move = input(f'{p}\'s turn.\nPlease indicate '
                         f'where you\'d like to move (1-9): ')
            try:
                m = int(move)
            except ValueError:
                print(f'Invalid input. Expected integer between 1-9')
                continue

            if m not in range(1, 10):
                print(f'Invalid input. Expected integer between 1-9')
                continue

            if board[m] == 'X' or board[m] == 'O':
                print(f'Invalid selection. That space is already occupied.')
                continue

            board[m] = marker

            print_board(board)
            if check_for_winner(board, player1, player2):
                return play_again(player1, player2)

            break

    print('Cat\'s game!\n')
    return play_again(player1, player2)


def check_for_winner(board, player1, player2):
    """
    Checks to see if there is a Tic Tac Toe.

    args:
        board (dict):   Holds all X & O info for gameplay
        player1 (str):  player1's name
        player2 (str):  player2's name
    """
    winner = False
    for combo in WIN_COMBOS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == 'X':
            print(f'Tic Tac Toe! {player1} wins!\n')
            winner = True
        elif board[combo[0]] == board[combo[1]] == board[combo[2]] == 'O':
            print(f'Tic Tac Toe! {player2} wins!\n')
            winner = True

    return winner


def play_again(player1, player2):
    """
    Checks if players want to play another game.

    args:
        player1 (str):  player1's name
        player2 (str):  player2's name
    """
    while True:
        play_game = input('Would you like to play again? (y/n): ')
        if play_game == 'y':
            return True
        elif play_game == 'n':
            return False
        else:
            print('Invalid input. Please type either "y" or "n"')


if __name__ == '__main__':
    main()
