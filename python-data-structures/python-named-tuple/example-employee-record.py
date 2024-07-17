from collections import namedtuple

Employee = namedtuple('Employee', ['name', 'age', 'title', 'department'])

# Create an employee record
emp = Employee('Alice', 30, 'Software Engineer', 'Development')

# Access fields
print(f'Employee Name: {emp.name}')        # Output: Employee Name: Alice
print(f'Employee Age: {emp.age}')          # Output: Employee Age: 30
print(f'Employee Title: {emp.title}')      # Output: Employee Title: Software Engineer
print(f'Department: {emp.department}')     # Output: Department: Development