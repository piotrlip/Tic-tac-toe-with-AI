from collections import deque
import random


def print_board(board_view):
    print('---------')
    print('| ' + ' '.join(board_view[0]) + ' |')
    print('| ' + ' '.join(board_view[1]) + ' |')
    print('| ' + ' '.join(board_view[2]) + ' |')
    print('---------')

    if command == 'start hard hard':
        print('Draw')

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

    elif len(move) > 2:
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

    elif len(move) > 2:
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


def isMovesLeft(board):
    for i1 in range(3):
        for j1 in range(3):
            if board[i1][j1] == ' ':
                return True
    return False


def evaluate(b):
    for row in range(3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == 'O':
                return 10
            elif b[row][0] == 'X':
                return -10

    for col in range(3):

        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

            if b[0][col] == 'O':
                return 10
            elif b[0][col] == 'X':
                return -10

    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

        if b[0][0] == 'O':
            return 10
        elif b[0][0] == 'X':
            return -10

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

        if b[0][2] == 'O':
            return 10
        elif b[0][2] == 'X':
            return -10
    return 0


def minimax(board, depth, isMax):
    score = evaluate(board)

    if score == 10:
        return score

    if score == -10:
        return score

    if isMovesLeft(board) == False:
        return 0

    if isMax:
        best = -1000

        for i2 in range(3):
            for j2 in range(3):

                if board[i2][j2] == ' ':
                    board[i2][j2] = 'O'
                    best = max(best, minimax(current_board, depth + 1, not isMax))
                    board[i2][j2] = ' '
        return best

    else:
        best = 1000

        for i3 in range(3):
            for j3 in range(3):

                if board[i3][j3] == ' ':
                    board[i3][j3] = 'X'
                    best = min(best, minimax(current_board, depth + 1, not isMax))
                    board[i3][j3] = ' '
        return best


def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):

            if board[i][j] == ' ':
                board[i][j] = 'O'
                moveVal = minimax(board, 0, False)
                board[i][j] = ' '

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove


def ai_move(level, current_board, counter):
    if level == 'easy':
        return random_move()

    elif level == 'medium':

        game_board_win = current_game_state(current_board)

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

    elif level == 'hard':
        bestMove = findBestMove(current_board)
        return [str(bestMove[0] + 1), str(bestMove[1] + 1)]


while True:
    command = input('Input command: ')
    good_commands = ['start easy easy', 'start easy user', 'start user user', 'start user easy', 'start medium user',
                     'start user medium', 'start user hard', 'start hard hard']
    if command in good_commands:
        level = None
        if 'easy' in command:
            level = 'easy'
        elif 'medium' in command:
            level = 'medium'
        else:
            level = 'hard'
        board = " " * 9
        current_board = cells_to_board(board)
        print_board(current_board)
        game_board = current_board
        counter = 0
        while True:
            if board_move(counter) == 'X':
                un_move = input('Enter the coordinates: ').split(' ')
                for i in un_move:
                    if i == '':
                        un_move.remove(i)
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
