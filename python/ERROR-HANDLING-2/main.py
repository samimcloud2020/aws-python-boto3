# 1. Runtime Error (occurs during execution)
def handle_runtime_error():
    try:
        # Attempting to divide by zero
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Runtime Error Caught: {e}")
    finally:
        print("Cleanup: This runs regardless of error")

# 2. Compile Error (syntax error preventing code from running)
# Note: This can't be caught with try-except as it prevents compilation
# The example below is commented to allow the program to run
# try:
#     print("Missing closing quote)  # SyntaxError: EOL while scanning string literal
# except SyntaxError as e:
#     print(f"Compile Error Caught: {e}")
# finally:
#     print("This won't run due to compile error")

# Instead, here's a valid example showing how to handle a potential syntax-related issue
def handle_compile_like_error():
    try:
        # Attempting to evaluate invalid Python code
        code = "print('incomplete"
        eval(code)
    except SyntaxError as e:
        print(f"Compile-like Error Caught: {e}")
    finally:
        print("Cleanup: Code evaluation completed")

# 3. Logical Error (code runs but produces incorrect results)
def handle_logical_error():
    try:
        # Logical error: incorrect formula for calculating average
        numbers = [1, 2, 3, 4, 5]
        wrong_average = sum(numbers) / 10  # Wrong divisor
        if wrong_average < 1:
            raise ValueError("Logical error: Average seems too low!")
        return wrong_average
    except ValueError as e:
        print(f"Logical Error Caught: {e}")
        # Correct the logical error
        correct_average = sum(numbers) / len(numbers)
        return correct_average
    finally:
        print("Cleanup: Logical error handling completed")

# Running the examples
print("1. Runtime Error Example:")
handle_runtime_error()
print("\n2. Compile-like Error Example:")
handle_compile_like_error()
print("\n3. Logical Error Example:")
result = handle_logical_error()
print(f"Corrected result: {result}")
