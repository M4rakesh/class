class Pupil:
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
print(pupil.get_age())
#pupil.__age=-1
#print(pupil.__age)
#pupil.set_age()