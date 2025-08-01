# Example: Reading and writing to a file using 'with'
try:
    # Writing to a file
    with open('example.txt', 'w') as file:
        file.write('Hello, this is a test!\n')
        file.write('Using the with statement is awesome!')
    print("File written successfully.")

    # Reading from the file
    with open('example.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print("Error: File not found.")
except IOError as e:
    print(f"Error: An I/O error occurred: {e}")
