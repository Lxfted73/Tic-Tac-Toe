# Tic Tac Toe Player

This Python module implements a Tic Tac Toe game player using the Minimax algorithm. The game is represented by a 3x3 board where two players, X and O, take turns to mark a space. The game ends when one player has three of their marks in a horizontal, vertical, or diagonal row or when the board is full.

## How to Use/How it works

1. **Starting the Game**: Use the `runner.py` file to get the starting state of the board, which is a 3x3 matrix filled with `None`, representing an empty board.

2. **Determining the Player**: The `player(board)` function returns which player has the next turn on a given board. It returns `X` if it's X's turn and `O` if it's O's turn.

3. **Valid Actions**: The `actions(board)` function returns a set of all possible actions (i, j) available on the board, where each action represents an empty space on the board that a player can mark.

4. **Resulting State**: The `result(board, action)` function returns the board state that results from making a move (i, j) on the board.

5. **Checking for a Winner**: The `winner(board)` function checks the board to determine if there is a winner. It returns `'X'` if player X has won, `'O'` if player O has won, or `None` if there is no winner yet.

6. **Game Termination**: The `terminal(board)` function checks if the game is over, either because there's a winner or because the board is full. It returns `True` if the game is over, `False` otherwise.

7. **Utility of the Game**: The `utility(board)` function evaluates the state of the board, returning 1 if X has won, -1 if O has won, and 0 for a tie or if the game is not yet finished.

8. **Minimax Algorithm**: The `minimax(board)` function determines the optimal move for the current player on the board. It returns the best action (i, j) according to the Minimax algorithm.
