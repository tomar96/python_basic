class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "python"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an Programmer")


e= Employee()
e.showDetails()
p= Programmer()
p.showDetails()