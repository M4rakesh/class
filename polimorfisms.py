class Pupil:
    __age=0
    #setter piekļuve cdatiem
    def set_age(self,value:int):
        self.__age=value
        #getter vērtības piešķiršana

pupil=Pupil()
pupil.__age=-1
print(pupil.__age)
#pupil.set_age()