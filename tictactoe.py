from collections import deque
import random


def print_board(board_view):
    print('---------')
    print('| ' + ' '.join(board_view[0]) + ' |')
    print('| ' + ' '.join(board_view[1]) + ' |')
    print('| ' + ' '.join(board_view[2]) + ' |')
    print('---------')


def cells_to_board(board):
    list_of_board = list(board)
    list_of_board_stack = deque(list_of_board)
    board_matrix_empty = [[' ' for _ in range(3)] for _ in range(3)]
    board_matrix = board_matrix_empty[:]
    for i in range(0, 3):
        for j in range(0, 3):
            board_matrix[i][j] = list_of_board_stack.popleft()
    return board_matrix


def coord_check(game_board, move):
    if len(move[0]) > 1:
        print('You should enter numbers!')
        return False

    elif len(move[1]) > 1:
        print('You should enter numbers!')
        return False

    elif int(move[0]) - 1 not in [0, 1, 2] or int(move[1]) - 1 not in [0, 1, 2]:
        print('Coordinates should be from 1 to 3!')
        return False
    elif game_board[int(move[0]) - 1][int(move[1]) - 1] != ' ':
        print('This cell is occupied! Choose another one!')
        return False
    else:
        return True


def board_move(counter):
    if counter in [0, 2, 4, 6, 8, 10]:
        return 'X'
    elif counter in [1, 3, 5, 7, 9, 11] != 0:
        return 'O'


def win_check(game_board):
    x_counter = 0
    y_counter = 0
    for i in game_board:
        for j in i:
            if j == 'X':
                x_counter += 1
            elif j == 'O':
                y_counter += 1

    game_board_wins = {'game_board_rows': {'first': ''.join(game_board[0]), 'second': ''.join(game_board[1]),
                                           'third': ''.join(game_board[2])},
                       'game_board_columns': {'first': ''.join([game_board[i][0] for i in range(3)]),
                                              'second': ''.join([game_board[i][1] for i in range(3)]),
                                              'third': ''.join([game_board[i][2] for i in range(3)])},
                       'game_board_diag': {'righ': ''.join([game_board[0][0], game_board[1][1], game_board[2][2]]),
                                           'left': ''.join([game_board[0][2], game_board[1][1], game_board[2][0]])}}

    if any('XXX' in d.values() for d in game_board_wins.values()) is True:
        return 'X wins'
    elif any('OOO' in d.values() for d in game_board_wins.values()) is True:
        return 'O wins'
    elif x_counter + y_counter == 9 and 'XXX' not in game_board_wins and 'OOO' not in game_board_wins:
        return 'Draw'
    elif x_counter + y_counter < 9 and 'XXX' not in game_board_wins and 'OOO' not in game_board_wins:
        return 'Making move level "easy"'


while True:
    command = input('Input command')
    good_commands = ['start easy easy', 'start easy user', 'start user user', 'start user easy']
    if command in good_commands:
        board = " " * 9
        current_board = cells_to_board(board)
        print_board(current_board)
        game_board = current_board
        counter = 0
        while True:
            if board_move(counter) == 'X':
                un_move = input('Enter the coordinates:').split(' ')
                if coord_check(current_board, un_move) is False:
                    continue
                else:
                    move = [int(un_move[0]) - 1, int(un_move[1]) - 1]
                    game_board[move[0]][move[1]] = 'X'
                    print_board(game_board)
                    counter += 1
                    print(win_check(game_board))
                    if win_check(game_board) == 'X wins' or win_check(game_board) == 'O wins' or win_check(
                            game_board) == 'Draw':
                        break
            elif board_move(counter) == 'O':
                while True:
                    move = [0, 0]
                    choice = [1, 2, 3]
                    move[0] = str(random.choice(choice))
                    move[1] = str(random.choice(choice))
                    if coord_check(current_board, move) is False:
                        continue
                    else:
                        break
                move = [int(move[0]) - 1, int(move[1]) - 1]
                game_board[int(move[0])][int(move[1])] = 'O'
                print_board(game_board)
                counter += 1
                print(win_check(game_board))
                if win_check(game_board) == 'X wins' or win_check(game_board) == 'O wins' or win_check(
                        game_board) == 'Draw':
                    break
                else:
                    continue

    elif command == 'exit':
        break

    else:
        print('Bad parameters!')
        continue
