
### Practical Use Case: 
File handling is a common task where with shines, as it guarantees the file is closed properly, preventing resource leaks.
### Error Handling: 
The example includes a try-except block to handle potential errors (e.g., file not found or I/O issues), showing how with integrates with robust code.
### Readability: 
The with statement makes the code concise and clear, avoiding manual calls to file.close().
### Safety: 
Even if an error occurs (e.g., permission issues), the file is automatically closed when the with block exits.

# Key Benefits of with

### Automatic Resource Management: 
No need to manually close resources like files or connections.
### Exception Safety: 
Ensures cleanup even if an error occurs.
### Concise Code: 
Reduces boilerplate code compared to try-finally blocks.

###################################################################################################
In Python, the with statement is used for resource management, ensuring that resources like files, sockets, or database connections are properly opened and closed, 
even if an error occurs. It simplifies exception handling and resource cleanup by using context managers. The with statement is commonly used with objects that 
support the context management protocol (i.e., have __enter__ and __exit__ methods).

## with context_manager as resource:
    # Code block where resource is used
    # Resource is automatically cleaned up after this block

### How It Works

The with statement sets up a context using the context manager.

The __enter__ method is called to initialize the resource, and its return value is assigned to the variable after as.

The code block inside the with executes.

The __exit__ method is called to clean up the resource (e.g., closing a file) when the block exits, whether normally or due to an exception.




# Custom Context Manager
You can create your own context manager using a class with __enter__ and __exit__ methods.

### class MyContextManager:

    def __enter__(self):
    
        print("Entering the context")
        
        return self  # Return object to be used in the 'as' clause
        
    def __exit__(self, exc_type, exc_value, traceback):
    
        print("Exiting the context")
        
        # Handle exceptions if needed
        
        if exc_type:
        
            print(f"An error occurred: {exc_value}")
            
        return False  # Let exceptions propagate

# Using the custom context manager

with MyContextManager() as cm:

    print("Inside the with block")
    
    # Simulate an error
    
    raise ValueError("Something went wrong!")
