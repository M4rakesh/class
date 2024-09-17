class Geom:
    name="Geom"

    def set_coords(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.draw()

    def draw(self):
        print("Ģeom.fig.zīmēšana")
class Line(Geom):
    name="Line"
    def draw(self):
        print("Līnijas zīmēšana")

'''class Rect(Geom):
    def draw(self):
        print("Taisnstūra zīmēšana")'''

class Rect(Geom):
    pass
    
#g=Geom()
l=Line()
r=Rect()
l.draw()
l.set_coords(1,5,12,3)
print(l.name)
r.draw()
r.set_coords(1,5,12,3)
print(r.name)
print(l.__dict__)
print(r.__dict__)
