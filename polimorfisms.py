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

class Animal:
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
    i.voice()