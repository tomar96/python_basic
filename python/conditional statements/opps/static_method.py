class employee:
    company= "google"
    def getSalary(self):
        print(f"salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning sir!")
    @staticmethod
    def time():
        print("time is 9am in the morning.")
harry= employee()

harry.salary = 100000
harry.greet()
timing=employee()
timing.time()
timing.company = "vishal"
