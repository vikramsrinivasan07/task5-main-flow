# Function to rotate a matrix by 90 degrees clockwise
def rotate_matrix(matrix):
    n = len(matrix)  # Size of the matrix (assuming it's a square matrix)
    
    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return matrix

# Input: Take a matrix from the user
n = int(input("Enter the size of the square matrix: "))
matrix = []

# Fill the matrix with user input
print(f"Enter the elements of the {n}x{n} matrix:")
for i in range(n):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    matrix.append(row)

# Rotate the matrix
rotated_matrix = rotate_matrix(matrix)

# Output the rotated matrix
print("Rotated matrix by 90 degrees clockwise:")
for row in rotated_matrix:
    print(row)
