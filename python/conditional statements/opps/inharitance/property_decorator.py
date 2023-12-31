class employee:
    company = "Bharat gas"

    salary = 5000
    bonus = 500

    @property
    def totalSalary(self):
        return self.salary + self.bonus


e = employee()
print(e.totalSalary)