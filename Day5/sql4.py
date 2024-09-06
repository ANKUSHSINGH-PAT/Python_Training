import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('day_5.db')
c = conn.cursor()

# '''
# # 1. Query to fetch all employees along with their department names
# c.execute('''
#           SELECT employees.name, employees.age, departments.name as department, employees.salary
#           FROM employees
#           JOIN departments ON employees.department_id = departments.id
#           ''')
# employees_with_departments = c.fetchall()
# print("Employees with Departments:", employees_with_departments)


# '''


# # 2. Query to fetch the average salary per department
# c.execute('''
#           SELECT departments.name, AVG(employees.salary) as avg_salary
#           FROM employees
#           JOIN departments ON employees.department_id = departments.id
#           GROUP BY departments.name
#           ''')
# average_salary_per_department = c.fetchall()
# print("Average Salary per Department:", average_salary_per_department)


# c.execute('''
#           SELECT departments.name, employees.name, MAX(employees.salary) as max_salary
#           FROM employees
#           JOIN departments ON employees.department_id = departments.id
#           GROUP BY departments.name
#           ''')
# highest_paid_employee_per_department = c.fetchall()
# print("Highest Paid Employee per Department:", highest_paid_employee_per_department)


# c.execute('''
#           SELECT departments.name, employees.name, Count(employees.id)
#           FROM employees
#           JOIN departments ON employees.department_id = departments.id
#           GROUP BY departments.name
#           ''')
# highest_paid_employee_per_department = c.fetchall()
# print("Highest Paid Employee per Department:", highest_paid_employee_per_department)


c.execute('''
          SELECT employees.name, employees.age, employees.salary
          FROM employees
          JOIN departments ON employees.department_id = departments.id
          WHERE departments.name = "Engineering"
          ''')
engineering_employees = c.fetchall()
print("Engineering Employees:", engineering_employees)

conn.close()