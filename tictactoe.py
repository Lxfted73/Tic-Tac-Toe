"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return terminal(board)
    x_count = 0
    o_count = 0
    for row in board:
        for column in row:
            if board[row][column] == X:
                x_count += 1
            elif board[row][column] == O:
                o_count += 1
            #In this case, the value is EMPTY
            elif board[row][column] == EMPTY:
                pass
            else:
                raise Exception("Row {row} and column {column} are not valid".format(row=row, column=column))

    if x_count == o_count:
        return X
    elif x_count == o_count + 1:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                action_set.add((row, col))

    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        return terminal(board)
    else:
        player_move = player(board)
        board_copy = copy.deepcopy(board)
        board_copy[action[0],action[1]] = player(board)
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Check Rows
    player_move = player(board)
    for row in board:
        if all(cell == player_move for cell in row):
            print(f"Player {player_move} has won the game by completing a row")
            return player_move

    for col in range(len(board[0])):
        if all(board[row][col] == player_move for row in range(3)):
            print(f"Player {player_move} has won the game by completing a col")
            return player_move

    if all(board[i][i] == player_move for i in range(3)):
        print(f"Player {player_move} has won the game by completing a Top to Bottom, Left to Right Diag")
        return player_move

    if all(board[i][3 - i] == player_move for i in range(3)):
        print(f"Player {player_move} has won the game by completing a Bottom to Top, Left to Right Diag")
        return player_move

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value, move = maxValue(board)
        return move
    else:
        value, move = minValue(board)
        return move

def maxValue(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    best_move = None
    for action in actions(board):
        move_eval, _ = minValue(result(board,action))
        if move_eval > v:
            v = move_eval
            best_move = action
        if v == 1:
            break
    return v, best_move

def minValue(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    best_move = None
    for action in actions(board):
        move_val, _ = maxValue(result(board, action))
        if move_val < v:
            v = move_val
            best_move = action
        if v == -1:
            break
    return v, best_move
    raise NotImplementedError