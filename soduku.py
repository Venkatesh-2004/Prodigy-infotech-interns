Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> // Here is a simple Sudoku solver code in Python:
... 
... def is_valid(board, row, col, num):
...     # Check if the number already exists in the row or column
...     for x in range(9):
...         if board[row][x] == num or board[x][col] == num:
...             return False
... 
...     # Check if the number exists in the 3x3 box
...     start_row = row - row % 3
...     start_col = col - col % 3
...     for i in range(3):
...         for j in range(3):
...             if board[i + start_row][j + start_col] == num:
...                 return False
... 
...     return True
... 
... def solve_sudoku(board):
...     for i in range(9):
...         for j in range(9):
...             if board[i][j] == 0:
...                 for num in range(1, 10):
...                     if is_valid(board, i, j, num):
...                         board[i][j] = num
...                         if solve_sudoku(board):
...                             return True
...                         board[i][j] = 0
...                 return False
...     return True
... 
... def print_board(board):
...     for i in range(9):
...         for j in range(9):
...             print(board[i][j], end=" ")
...             if (j + 1) % 3 == 0 and j < 8:
...                 print("| ", end="")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print("- - - - - - - - - - -")

# Test the solver
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print_board(board)
else:
    print("No solution exists")
