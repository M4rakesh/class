class Table:
    def __init__(self,l=1,w=1,h=1):
        self.lenght=l
        self.width=w
        self.height=h
        if isinstance(self,KitchenTable):
            p = int(input("Cik vietu:     "))
            self.plasces=p
            print(f"{self.plasces}")

    def info_table(self):
        print(f"Leght: {self.lenght},Width:{self.width},Height:{self.height}")


class DeskTable(Table):
    def square(self):
        return self.width * self.lenght
    

class CompuerTable(DeskTable):
    def square(self,monitor=0.0):
        return self.width*self.lenght-monitor
    
'''class KitchenTaable(Table):
    def __init__(self, l, w, h,p):
        Table.__init__(self,l, w, h)
        self.places = p
        print(f"Place:{self.places}")
class KitchenTaable(Table):
    def __init__(self, l, w, h,p):
        super().__init__(l, w, h)
        self.places = p
        print(f"Place:{self.places}")'''
class KitchenTable(Table):
    pass


t1= Table(1.5,1.8,0.75)
t1.info_table()
t2=DeskTable(0.8,0.6,0.7)
print(t2.square())
t2.info_table
t3=CompuerTable(0.8,0.6,0.7)
print(t3.square(0.3))   
t4=KitchenTaable(1.5,2,0.75)
t4.info_table()