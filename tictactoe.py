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
        board_copy[action(0), action(1)] = player(board)
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

    for col in range(len(board[0])):
        if all(board[row][col] == player_move for row in range(3)):
            print(f"Player {player_move} has won the game by completing a col")

    if all(board[i][i] == player_move for i in range(3)):
        print(f"Player {player_move} has won the game by completing a Top to Bottom, Left to Right Diag")

    if all(board[i][3 - i] == player_move for i in range(3)):
        print(f"Player {player_move} has won the game by completing a Bottom to Top, Left to Right Diag")

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        word_count = 0
        for row in board():
            for column in row:
                if column == X or O:
                    word_count += 1
    if word_count == 9:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        else:
            return -1
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    raise NotImplementedError