import mysql.connector
from mysql.connector import Error

try:
    # Using 'with' to manage database connection
    with mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    ) as connection:
        # Create a cursor to execute queries
        with connection.cursor() as cursor:
            # Example query: Select all records from a table
            cursor.execute("SELECT * FROM employees")
            result = cursor.fetchall()
            
            # Print results
            print("Employee Records:")
            for row in result:
                print(row)
                
        # Connection is automatically committed if no errors occur
        connection.commit()

except Error as e:
    print(f"Error connecting to MySQL: {e}")

# No need to explicitly close the connection; 'with' handles it


########pip install mysql-connector-python
