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
        return X
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
            #In this case, the value is EMPTY
            elif cell == EMPTY:
                pass
            else:
                raise Exception("Row {row} and column {column} are not valid".format(row=row, column=cell))

    if x_count == o_count:
        return X
    elif x_count == o_count + 1:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
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
    row, col = action
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != EMPTY:
        # If the action is out of bounds or the position is already taken, raise an exception
        raise ValueError("Invalid action: Out of bounds or position already taken")

    else:
        player_move = player(board)
        board_copy = copy.deepcopy(board)
        board_copy[row][col] = player(board)
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if all(cell == X for cell in row):
            print(f"Player X has won the game by completing a row")
            return X

    for col in range(3):
        if all(board[row][col] == X for row in range(3)):
            print(f"Player X has won the game by completing a col")
            return X

    if all(board[i][i] == X for i in range(3)):
        print(f"Player X has won the game by completing a Top to Bottom, Left to Right Diag")
        return X

    if all(board[i][2 - i] == X for i in range(3)):
        print(f"Player X has won the game by completing a Bottom to Top, Left to Right Diag")
        return X

    for row in board:
        if all(cell == O for cell in row):
            print(f"Player O has won the game by completing a row")
            return O



    for col in range(3):
        if all(board[row][col] == O for row in range(3)):
            print(f"Player O has won the game by completing a col")
            return O

    if all(board[i][i] == O for i in range(3)):
        print(f"Player X has won the game by completing a Top to Bottom, Left to Right Diag")
        return O

    if all(board[i][2 - i] == X for i in range(3)):
        print(f"Player X has won the game by completing a Bottom to Top, Left to Right Diag")
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        if any(EMPTY in row for row in board):
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
        _, move = maxValue(board)
        return move
    else:
        _, move = minValue(board)
        return move

def maxValue(board):
    if terminal(board):
        return utility(board), None
    v = float('-inf')
    best_move = None
    for action in actions(board):
        move_eval, _ = minValue(result(board,action))
        if move_eval > v:
            v = move_eval
            best_move = action
        if v == 1:
            return v, best_move
    return v, best_move

def minValue(board):
    if terminal(board):
        return utility(board), None
    v = float('inf')
    best_move = None
    for action in actions(board):
        move_val, _ = maxValue(result(board, action))
        if move_val < v:
            v = move_val
            best_move = action
        if v == -1:
            return v, best_move
    return v, best_move