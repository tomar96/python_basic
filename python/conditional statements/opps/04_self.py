class employee:
    company= "google"
    def getSalary(self):
        print(f"salary is {self.salary}")
harry= employee()

harry.salary = 100000
harry.getSalary()