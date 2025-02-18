# Function to find the N-th Fibonacci number using Dynamic Programming
def fibonacci(n):
    # Handle base cases
    if n <= 1:
        return n
    
    # Initialize a list to store Fibonacci numbers up to n
    fib = [0] * (n + 1)
    
    # Base cases
    fib[0] = 0
    fib[1] = 1
    
    # Fill the fib array using dynamic programming
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    # Return the N-th Fibonacci number
    return fib[n]

# Input: Get the N-th Fibonacci number
n = int(input("Enter a number N to find the N-th Fibonacci number: "))
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
