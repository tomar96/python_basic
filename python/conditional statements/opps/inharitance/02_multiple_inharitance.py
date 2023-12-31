class Employee:
    company="google"
    eCode = 200


class freeLancer:
    company= "Fiver"
    level = 0
    def upgradeLevel(self):
        self.level=self.level+1

class Programmer (Employee,freeLancer):
    name = "Rohit"

p=Programmer()
print(p.company)
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company)