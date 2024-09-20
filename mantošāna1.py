class Veicle:
    total=0
    def __init__(self,make,model,year,price):
        self.make=make
        self.model=model
        self.year=year
        self.price=price
    def total_vehicles(self):
        Veicle.total+=self.price
        print(f"Auto cena ir {Veicle.total}")
        return Veicle.total
    def display_info(self):
        print(f"Marka;{self.make},Model:{self.model},Year:{self.year},Price:{self.price}")
class Car(Veicle):
    def __init__(self,make,model,year,price,num_doors,body_style):
        super().__init__(make,model,year,price)
        self.num_doors=num_doors
        self.body_style=body_style
    def display_info(self):
        print(f"Marka;{self.make},Model:{self.model},Year:{self.year},Price:{self.price},Doors:{self.num_doors},Body Type:{self.body_style}")
class Truck(Veicle):
    def __init__(self,make,model,year,price,bed_leght,towing_capacity):
        super().__init__(make,model,year,price)
        self.bed_leght=bed_leght
        self.towing_capacity=towing_capacity
    def display_info(self):
        print(f"Marka;{self.make},Model:{self.model},Year:{self.year},Price:{self.price},Bed leght:{self.bed_leght},towing capacity:{self.towing_capacity}")

a=Car("Audi","a6",2006,3400,5,"universals")
a.display_info()
a.total_vehicles()
truck=Truck("Ford","FM106",2023,30000,"6162","13 t")
truck.display_info()
truck.total_vehicles()

# Virsklase (Superklase)
class Dzivnieks:
    def __init__(self, vards):
        self.vards = vards

    def skaņas(self):
        return "Nezināma skaņa"

    def iepazīstināt(self):
        return f"Es esmu {self.vards} un es izsaku: {self.skaņas()}"


# Apakšklase (Subklase) - mantošana no Dzivnieks
'''class Suns(Dzivnieks):
    def __init__(self, vards, šķirne):
        super().__init__(vards)  # Izsauc virsklases konstruktoru
        self.šķirne = šķirne

    def skaņas(self):
        return "Vau"

    def iepazīstināt(self):
        return f"Es esmu {self.vards}, esmu {self.šķirne} šķirnes suns un es izsaku: {self.skaņas()}"


# Apakšklase (Subklase) - mantošana no Dzivnieks
class Kaķis(Dzivnieks):
    def __init__(self, vards, vecums):
        super().__init__(vards)  # Izsauc virsklases konstruktoru
        self.vecums = vecums

    def skaņas(self):
        return "Mjaū"

    def iepazīstināt(self):
        return f"Es esmu {self.vards}, man ir {self.vecums} gadi un es izsaku: {self.skaņas()}"


# Izmantošana
suns = Suns("Riks", "Labradors")
kakis = Kaķis("Mija", 5)

print(suns.iepazīstināt())
print(kakis.iepazīstināt())'''