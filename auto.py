class Veicle:
    def __init__(self,make,model,year,price):
        self.make=make
        self.model=model
        self.year=year
        self.price=price

    def display_info(self):
        print(f"Marka;{self.make},Model:{self.model},Year:{self.year},Price:{self.price}")
class Car:
    def __init__(self,make,model,year,price,num_doors,body_style):
        super().__init__(make,model,year,price)
        self.num_doors=num_doors
        self.body_style=body_style
a=Veicle("Audi","a6",2006,3400,5,"universals")
a.display_info()
