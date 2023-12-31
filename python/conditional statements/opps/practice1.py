class Programmers:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getdata(self):
        print(f"Employee name is {self.name}")
        print(f"Product is {self.product}")

aakanshu=Programmers("Aakanshu","Mobile")
aakanshu.getdata()
Himani=Programmers("HImani","laptop")
Himani.getdata()