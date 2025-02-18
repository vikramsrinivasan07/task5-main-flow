# Function to find duplicates in a list
def find_duplicates(input_list):
    # Use a dictionary to count occurrences of each element
    element_count = {}
    
    # Loop through the list and count elements
    for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    # List to store duplicates
    duplicates = [element for element, count in element_count.items() if count > 1]
    
    return duplicates

# Input: Take list input from the user
input_list = list(map(int, input("Enter a list of numbers (space-separated): ").split()))

# Find duplicates
duplicates = find_duplicates(input_list)

# Output the result
if duplicates:
    print(f"Duplicates in the list: {duplicates}")
else:
    print("No duplicates found.")
