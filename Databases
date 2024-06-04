9. SQL Basics 
Write a SQL query to create a table `students` with columns `id`, `name`, and `grade`. 10. 

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    grade VARCHAR(10)
);

10. Write a Python function `insert_student(name: str, grade: float)` that inserts a new  student into the `students` table using SQLite. 

import sqlite3

def insert_student(name: str, grade: float):
    # Connect to the SQLite database
    connection = sqlite3.connect('your_database_name.db')  # Replace 'your_database_name.db' with your actual database name

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Define the SQL query to insert a new student
    query = "INSERT INTO students (name, grade) VALUES (?, ?)"

    # Execute the query with the provided parameters
    cursor.execute(query, (name, grade))

    # Commit the transaction
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()

# Example usage:
insert_student("John Doe", 85.5)

