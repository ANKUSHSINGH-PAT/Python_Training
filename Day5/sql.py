import sqlite3

# Create a connection to the database
conn = sqlite3.connect('test1.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Query to get the name of the employee with emp_id = 6
# query = "select employee_name from Employee WHERE emp_id = 6"
query = "select employee_name,department FROM Employee WHERE salary > 80000 or emp_id <6"
# query = "select department, count(emp_id) FROM Employee WHERE salary < 80000 group by department having age>29 "

# Execute the query
cursor.execute(query)

# Fetch the result
result = cursor.fetchall()

# Print the name of the employee
if result:
    print("Output of query is", result)
else:
    print("No record ")

# Close the connection
conn.close()


#display department and count with salary < 80000