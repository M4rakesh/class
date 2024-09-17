class Veicle:
    def __init__(self,make,model,year,price):
        self.make=make
        self.model=model
        self.year=year
        self.price=price

    def display_info(self):
        print(f"Marka;{self.make},Model:{self.model},Year:{self.year},Price:{self.price}")

a=Veicle("Audi","a6",2006,3400)
a.display_info()