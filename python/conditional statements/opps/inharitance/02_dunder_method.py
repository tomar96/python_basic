class Number:
    def __init__(self,num):
        self.num= num

    def __add__(self,num2):
        print("lets add")
        return self.num + num2.num

    def __mul__(self,num2):
        print("lets add")
        return self.num * num2.num

    def __str__(self):
        return f"the Decimal number is:{self.num}"


n1= Number(6)
print(n1)