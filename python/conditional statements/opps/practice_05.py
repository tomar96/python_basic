class Train():
    def __init__(self,name,fare,seats):
        self.name= name
        self.fare= fare
        self.seats= seats

    def getstatus(self):
        print("--------------------")
        print(f"The train name is {self.name}")
        print(f"The available seats are {self.seats}")
        print("--------------------")

    def FareInfo(self):
        print(f"The Fare is Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print("The ticket is booked")
            self.seats=self.seats-1
        else:
            print("Sorry!,The Train is FULL")

Intercity=Train("Intercity : 100256",90,200)
Intercity.getstatus()
Intercity.FareInfo()
Intercity.bookTicket()
Intercity.getstatus()