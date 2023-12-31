
class RailwayForm:
    formType= "RailwayForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")

aakanshuApplication = RailwayForm()
aakanshuApplication.name = "Aakanshu"
aakanshuApplication.train = "Gardwal"
aakanshuApplication.printData() 