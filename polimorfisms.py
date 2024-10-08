'''class Pupil:
    __age=0
    #setter piekļuve cdatiem
    def set_age(self,value:int):
        if value>=0:
            self.__age=value
        else:
            print("Vecums nevar būt nagatīvs")
        #getter vērtības piešķiršana
    def get_age(self):
        return self.__age
    
    
pupil=Pupil()
pupil.set_age(-1)
pupil.set_age(10)
print(pupil.get_age())'''
#pupil.__age=-1
#print(pupil.__age)
#pupil.set_age()

'''class Animal:
    legs=4
    tail=1

    def voice(self):
        return
    

class Cat(Animal):
    def cat_voice(self):
        print("Mjau")


class Dog(Animal):
    def dog_voice():
        print("Gav")


class Cow(Animal):
    def cow_voice():
        print("Muuu")


a=Animal()
a.voice()
cat1,cat2=Cat(),Cat()
dog1,dog2=Dog(),Dog()
cow1,cow2=Cow(),Cow()

farm_band=[cat1,cat2,dog1,dog2,cow1,cow2]
for i in farm_band:
    if isinstance(i,Cat):
        i.cat_voice()
    if isinstance(i,Dog):
        i.dog_voice()
    if isinstance(i,Cow):
        i.cow_voice()'''

'''class Animal:
    legs=4
    tail=1

    def voice(self):
        print("Kaut-kāda skaņa")
    

class Cat():
    def voice(self):
        print("Mjau")


class Dog():
    def voice(self):
        print("Gav")


class Cow():
    def voice(self):
        print("Muuu")


a=Animal()
a.voice()
cat1,cat2=Cat(),Cat()
dog1,dog2=Dog(),Dog()
cow1,cow2=Cow(),Cow()

farm_band=[cat1,cat2,dog1,dog2,cow1,cow2]
for i in farm_band:
    i.voice()'''
import math
class Shape:
    def area(self):
        pass
    def perimetr(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height
    def perimetr(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):

    def __init__(self,radiuss):
        self.radiuss=radiuss
    def perimetr(self):
        return 2*math.pi * self.radiuss
    def area(self):
        return (math.pi * self.radiuss**2)
    
c1=Circle(1.5)
print(c1.area())
print(c1.perimetr())

shapes=[Rectangle(3,4),Circle(5)]
for shape in shapes:
    print(f"Area:{shape.area():.2f},Perimetr:{shape.perimetr():.2f}")