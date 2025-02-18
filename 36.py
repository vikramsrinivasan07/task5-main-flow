# Function to find the length of the Longest Increasing Subsequence (LIS)
def longest_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at index i
    dp = [1] * n

    # Fill the dp array
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest increasing subsequence will be the max value in dp
    return max(dp)

# Input: Take a list of integers from the user
arr = list(map(int, input("Enter a list of numbers (space-separated): ").split()))

# Find the length of the longest increasing subsequence
result = longest_increasing_subsequence(arr)

# Output the result
print(f"The length of the Longest Increasing Subsequence is: {result}")
