class employee:
    company= "google"


    def __init__(self, name, salary, subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("employee is created")
    def GetDetails(self):
        print(f"The name is:{self.name}")
        print(f"The salary is:{self.salary}")
        print(f"The subunit is:{self.subunit}")

    def getSalary(self):
        print(f"salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning sir!")
    @staticmethod
    def time():
        print("time is 9am in the morning.")
harry= employee("rahul",2000,"canon")
harry.GetDetails()
