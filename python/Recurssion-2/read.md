Recursion in Python is when a function calls itself to solve a problem by breaking it into smaller instances of the same problem. Here's a clear example using **factorial** calculation:

```python
def factorial(n):
    # Base case: stops recursion
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)
```

### Explanation:
- **Base case**: When `n` is 0 or 1, return 1 (stops recursion).
- **Recursive case**: For `n > 1`, the function computes `n * factorial(n-1)`, calling itself with a smaller input.
- For `factorial(5)`:
  - 5 * factorial(4)
  - 5 * (4 * factorial(3))
  - 5 * (4 * (3 * factorial(2)))
  - 5 * (4 * (3 * (2 * factorial(1))))
  - 5 * (4 * (3 * (2 * 1))) = 120

### Key Points:
- Always define a **base case** to prevent infinite recursion.
- Recursion can be memory-intensive; Python has a default recursion limit (typically 1000).
- Use recursion for problems like tree traversal, factorial, or Fibonacci, but consider iterative solutions for efficiency in some cases.

Want another example, like Fibonacci or a tree traversal?
