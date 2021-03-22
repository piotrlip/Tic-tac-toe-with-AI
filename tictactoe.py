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


def coord_check_o(game_board, move):
    if len(move[0]) > 1:
        return False

    elif len(move[1]) > 1:
        return False

    elif int(move[0]) - 1 not in [0, 1, 2] or int(move[1]) - 1 not in [0, 1, 2]:
        return False
    elif game_board[int(move[0]) - 1][int(move[1]) - 1] != ' ':
        return False
    else:
        return True


def board_move(counter):
    if counter in [0, 2, 4, 6, 8, 10]:
        return 'X'
    elif counter in [1, 3, 5, 7, 9, 11] != 0:
        return 'O'


def current_game_state(game_board):
    current_state = {'game_board_rows': {'first': ''.join(game_board[0]), 'second': ''.join(game_board[1]),
                                         'third': ''.join(game_board[2])},
                     'game_board_columns': {'first': ''.join([game_board[i][0] for i in range(3)]),
                                            'second': ''.join([game_board[i][1] for i in range(3)]),
                                            'third': ''.join([game_board[i][2] for i in range(3)])},
                     'game_board_diag': {'righ': ''.join([game_board[0][0], game_board[1][1], game_board[2][2]]),
                                         'left': ''.join([game_board[0][2], game_board[1][1], game_board[2][0]])}}
    return current_state


def win_check(game_board, level):
    x_counter = 0
    y_counter = 0
    for i in game_board:
        for j in i:
            if j == 'X':
                x_counter += 1
            elif j == 'O':
                y_counter += 1

    game_board_wins = current_game_state(game_board)

    if any('XXX' in d.values() for d in game_board_wins.values()) is True:
        return 'X wins'
    elif any('OOO' in d.values() for d in game_board_wins.values()) is True:
        return 'O wins'
    elif x_counter + y_counter == 9 and 'XXX' not in game_board_wins and 'OOO' not in game_board_wins:
        return 'Draw'
    elif x_counter + y_counter < 9 and 'XXX' not in game_board_wins and 'OOO' not in game_board_wins:
        return f'Making move level "{level}"'


def random_move():
    move = [0, 0]
    choice = [1, 2, 3]
    move[0] = str(random.choice(choice))
    move[1] = str(random.choice(choice))
    return move


def ai_move(level, current_board, counter):
    if level == 'easy':
        return random_move()

    elif level == 'medium':

        game_board_win = current_game_state(current_board)

        coord_current = {'00': current_board[0][0], '01': current_board[0][1], '02': current_board[0][2],
                         '10': current_board[1][0], '11': current_board[1][1], '12': current_board[1][2],
                         '20': current_board[2][0], '21': current_board[2][1], '22': current_board[2][2]}

        current_moves = {'game_board_rows': {'first': [current_board[0][0], current_board[0][1], current_board[0][2]],
                                             'second': [current_board[1][0], current_board[1][1], current_board[1][2]],
                                             'third': [current_board[2][0], current_board[2][1], current_board[2][2]]},

                         'game_board_columns': {
                             'first': [current_board[0][0], current_board[1][0], current_board[2][0]],
                             'second': [current_board[0][1], current_board[1][1], current_board[2][1]],
                             'third': [current_board[0][2], current_board[1][2], current_board[2][2]]},

                         'game_board_diag': {'righ': [current_board[0][0], current_board[1][1], current_board[2][2]],
                                             'left': [current_board[0][2], current_board[1][1], current_board[2][0]]}}

        win_moves = {'game_board_rows': {'first': [['0', '0'], ['0', '1'], ['0', '2']],
                                         'second': [['1', '0'], ['1', '1'], ['1', '2']],
                                         'third': [['2', '0'], ['2', '1'], ['2', '2']]},
                     'game_board_columns': {'first': [['0', '0'], ['1', '0'], ['2', '0']],
                                            'second': [['1', '0'], ['1', '1'], ['1', '2']],
                                            'third': [['2', '0'], ['2', '1'], ['2', '2']]},
                     'game_board_diag': {'righ': [['0', '0'], ['1', '1'], ['2', '2']],
                                         'left': [['0', '2'], ['1', '1'], ['2', '0']]}}

        possible_moves = {'game_board_rows': {'first': [],
                                              'second': [],
                                              'third': []},
                          'game_board_columns': {'first': [],
                                                 'second': [],
                                                 'third': []},
                          'game_board_diag': {'righ': [],
                                              'left': []}}

        for key3, value3 in current_moves.items():
            for key4, value4 in value3.items():
                for i in range(len(value4)):
                    if value4[i] not in ['X', 'O']:
                        possible_moves[key3][key4].append(win_moves[key3][key4][i])

        possible_moves_x = {'game_board_rows': {'first': [],
                                                'second': [],
                                                'third': []},
                            'game_board_columns': {'first': [],
                                                   'second': [],
                                                   'third': []},
                            'game_board_diag': {'righ': [],
                                                'left': []}}
        possible_moves_o = {'game_board_rows': {'first': [],
                                                'second': [],
                                                'third': []},
                            'game_board_columns': {'first': [],
                                                   'second': [],
                                                   'third': []},
                            'game_board_diag': {'righ': [],
                                                'left': []}}
        for key1, value1 in game_board_win.items():
            for key2, value2 in value1.items():
                if 'XX' in value2:
                    possible_moves_x[key1][key2].append('OK')
                if 'OO' in value2:
                    possible_moves_o[key1][key2].append('OK')

        # winning AI
        move_with_o = []
        for key5, value5 in possible_moves_o.items():
            for key6, value6 in value5.items():
                if 'OK' in value6 and len((''.join(current_moves[key5][key6])).replace(' ', '', 2)) < 3:
                    move_with_o.append(possible_moves[key5][key6][0])

        # blocking user
        move_with_x = []
        for key5, value5 in possible_moves_x.items():
            for key6, value6 in value5.items():
                if 'OK' in value6 and 2 <= len((''.join(current_moves[key5][key6])).replace(' ', '', 2)) < 3:
                    move_with_x.append(possible_moves[key5][key6][0])

        if len(move_with_o) != 0:
            a = random.choice(move_with_o)
            b = [str(int(a[0]) + 1), str(int(a[1]) + 1)]
            return b

        elif len(move_with_x) != 0:
            a = random.choice(move_with_x)
            b = [str(int(a[0]) + 1), str(int(a[1]) + 1)]
            return b
        else:
           return random_move()


while True:
    command = input('Input command: ')
    good_commands = ['start easy easy', 'start easy user', 'start user user', 'start user easy', 'start medium user',
                     'start user medium']
    if command in good_commands:
        level = None
        if 'easy' in command:
            level = 'easy'
        else:
            level = 'medium'
        board = " " * 9
        current_board = cells_to_board(board)
        print_board(current_board)
        game_board = current_board
        counter = 0
        while True:
            if board_move(counter) == 'X':
                un_move = input('Enter the coordinates: ').split(' ')
                if coord_check(current_board, un_move) is False:
                    continue
                else:
                    move = [int(un_move[0]) - 1, int(un_move[1]) - 1]
                    game_board[move[0]][move[1]] = 'X'
                    print_board(game_board)
                    counter += 1
                    print(win_check(game_board, level))
                    if win_check(game_board, level) == 'X wins' or win_check(game_board,
                                                                             level) == 'O wins' or win_check(game_board,
                                                                                                             level) == 'Draw':
                        break
            elif board_move(counter) == 'O':
                while True:
                    move = ai_move(level, current_board, counter)
                    if coord_check_o(current_board, move) is False:
                        continue
                    else:
                        break
                move = [int(move[0]) - 1, int(move[1]) - 1]
                game_board[int(move[0])][int(move[1])] = 'O'
                print_board(game_board)
                counter += 1
                print(win_check(game_board, level))
                if win_check(game_board, level) == 'X wins' or win_check(game_board, level) == 'O wins' or win_check(
                        game_board, level) == 'Draw':
                    break
                else:
                    continue

    elif command == 'exit':
        break

    else:
        print('Bad parameters!')
        continue
