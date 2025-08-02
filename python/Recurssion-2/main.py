def factorial(n):
    # Base case: stops recursion
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)
