class Person:
    country= "India"

    def takeBreath(self):
        print("i am breathing...")

class Employee(Person):
    company = "Fiver"

    def getSalary(self):
        print(f"Salary is {self.getSalary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an employee so i am breathing..")

class Programmer(Employee):
    company="honda"
    def getSalary(self):
        print(f"No salary to programmer")


    def takeBreath(self):
        super().takeBreath()
        print("I am an programmer so i am breathing++..")


p= Person()
p.takeBreath()
e= Employee()
e.takeBreath()
pr= Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)