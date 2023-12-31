class Employee:
    company="Google"
    salary = 100


harry= Employee()
ram= Employee()
print(harry.company)
print(ram.company)
harry.salary =300
ram.salary = 400
Employee.company="youtube"
print(harry.company)
print(ram.company)
print(harry.salary)
print(ram.salary)
