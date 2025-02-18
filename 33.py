import itertools

# Function to generate permutations
def generate_permutations():
    # Take input from the user
    input_string = input("Enter a string: ")
    
    # Generate all permutations using itertools.permutations
    permutations = itertools.permutations(input_string)
    
    # Print the permutations
    print("Permutations of the string are:")
    for perm in permutations:
        print(''.join(perm))

# Call the function to generate permutations
generate_permutations()
