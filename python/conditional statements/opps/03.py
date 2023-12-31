class Employee:
    company = "Google"
    salary = 100 
Harry = Employee()
rajini = Employee()
Harry.salary = 300
rajini.salary = 400
print(Harry.company)
Employee.company = "youtube"
print(rajini.company)
print(Harry.salary)
print(rajini.salary)