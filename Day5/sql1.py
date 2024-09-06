import sqlite3

# Create a connection to the database (or create if it doesn't exist)
conn = sqlite3.connect('test1.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the employee table '', " hi "How are you", i am fine" ''' '''
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee (
        emp_id INTEGER PRIMARY KEY,
        employee_name TEXT,
        age INTEGER,
        department TEXT,
        year_of_experience INTEGER,
        salary REAL
    )
''')

# Dummy data
dummy_data = [
    (1, 'John Doe', 30, 'Automation', 5, 60000.00),
    (2, 'Jane Smith', 28, 'Automation', 3, 55000.00),
    (3, 'Michael Johnson', 35, 'Automation', 7, 70000.00),
    (4, 'Emily Brown', 32, 'Automation', 4, 62000.00),
    (5, 'David Wilson', 33, 'Automation', 6, 65000.00),
    (6, 'Sarah Williams', 31, 'SAP', 6, 72000.00),
    (7, 'Daniel Taylor', 29, 'SAP', 4, 60000.00),
    (8, 'Olivia Martinez', 34, 'SAP', 8, 80000.00),
    (9, 'James Jones', 36, 'Salesforce', 9, 85000.00),
    (10, 'Emma Garcia', 27, 'Salesforce', 2, 50000.00)
]

# Insert dummy data into the table
cursor.executemany('''
    INSERT INTO employee (emp_id, employee_name, age, department, year_of_experience, salary)
    VALUES (?, ?, ?, ?, ?, ?)
''', dummy_data)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Database 'test1.db' created with table 'employee' and dummy data inserted.")