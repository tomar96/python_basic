class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"The square of the {self.num} is {self.num **2}")

    def squareRoot(self):
        print(f"The squareRoot of the {self.num} is {self.num **0.5}")

    def cube(self):
        print(f"The cube of the {self.num} is {self.num **3}")

a = Calculator(6666)
a.square()
a.cube()
a.squareRoot()