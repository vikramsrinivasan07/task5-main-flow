# Function to find K largest elements using sorting
def k_largest_elements(arr, k):
    # Sort the array in descending order and return the first K elements
    return sorted(arr, reverse=True)[:k]

# Input: Take a list of numbers and K value from the user
arr = list(map(int, input("Enter a list of numbers (space-separated): ").split()))
k = int(input("Enter the value of K: "))

# Find the K largest elements
result = k_largest_elements(arr, k)

# Output the result
print(f"The {k} largest elements are: {result}")
