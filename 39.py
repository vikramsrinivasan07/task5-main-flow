# Function to check if a given Sudoku board is valid
def is_valid_sudoku(board):
    # Check each row
    for row in board:
        if not is_valid_row(row):
            return False
    
    # Check each column
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_row(column):
            return False
    
    # Check each 3x3 subgrid
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(board[row + i][col + j])
            if not is_valid_row(subgrid):
                return False

    # If all checks pass
    return True

# Helper function to check if a row, column, or subgrid is valid
def is_valid_row(group):
    # Filter out the empty cells (represented by '.')
    filtered_group = [x for x in group if x != '.']
    # Check if there are any duplicates in the filtered group
    return len(filtered_group) == len(set(filtered_group))

# Input: Take the Sudoku board as a 2D list (9x9)
print("Enter the Sudoku board (use '.' for empty cells):")
board = []
for i in range(9):
    row = input(f"Enter row {i+1}: ").split()
    board.append(row)

# Validate the Sudoku board
if is_valid_sudoku(board):
    print("The Sudoku board is valid.")
else:
    print("The Sudoku board is invalid.")
