import sqlite3
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('day_5.db')
c = conn.cursor()
# Create the departments table
c.execute('''
          CREATE TABLE IF NOT EXISTS departments
          (id INTEGER PRIMARY KEY,
          name TEXT)
          ''')
# Insert data into the departments table
departments = [
    (1, 'HR'),
    (2, 'Engineering'),
    (3, 'Sales'),
    (4, 'Marketing')
]
c.executemany('INSERT INTO departments (id, name) VALUES (?, ?)', departments)
# Create the employees table
c.execute('''
          CREATE TABLE IF NOT EXISTS employees
          (id INTEGER PRIMARY KEY,
          name TEXT,
          age INTEGER,
          department_id INTEGER,
          salary REAL,
          FOREIGN KEY (department_id) REFERENCES departments (id))
          ''')
# Insert data into the employees table
employees = [
    ('Alice', 30, 1, 70000),
    ('Bob', 35, 2, 80000),
    ('Charlie', 25, 3, 50000),
    ('David', 40, 2, 90000),
    ('Eva', 28, 4, 60000),
    ('Frank', 50, 1, 75000),
    ('Grace', 32, 2, 85000),
    ('Hank', 45, 3, 55000),
    ('Ivy', 29, 4, 62000),
    ('John', 38, 2, 95000)
]
c.executemany('INSERT INTO employees (name, age, department_id, salary) VALUES (?,?,?,?)', employees)
# Commit the changes and close the connection

conn.commit()
conn.close()