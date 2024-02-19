"""
Tic Tac Toe Player
"""

import math

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
        for column in board[row]:
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
    else:
        raise Exception("x_count {x_count} and o_count {o_count} are not valid".
                        format(x_count=x_count, o_count=o_count))

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
