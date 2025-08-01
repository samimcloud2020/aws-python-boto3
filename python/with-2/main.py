import sqlite3

try:
    # Using 'with' to manage SQLite database connection
    with sqlite3.connect("company.db") as connection:
        # Create a cursor to execute queries
        with connection.cursor() as cursor:
            # Create employees table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    department TEXT,
                    salary REAL
                )
            """)
            
            # Insert sample data (only if table is newly created)
            cursor.execute("INSERT OR IGNORE INTO employees (name, department, salary) VALUES (?, ?, ?)", 
                          ("John Doe", "IT", 75000.0))
            cursor.execute("INSERT OR IGNORE INTO employees (name, department, salary) VALUES (?, ?, ?)", 
                          ("Jane Smith", "HR", 65000.0))
            
            # Commit the table creation and inserts
            connection.commit()
            
            # Example query: Select all records from employees table
            cursor.execute("SELECT * FROM employees")
            result = cursor.fetchall()
            
            # Print results
            print("Employee Records:")
            for row in result:
                print(row)

except sqlite3.Error as e:
    print(f"Error with SQLite database: {e}")

# No need to explicitly close the connection; 'with' handles it
