# Inheritance : 

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod   # abstract methods dont have thier own implementation.. the class which inherit them give there implementation.
    def sound():
        pass

class Bird(Animal,ABC):   # level 1 inheritance    # we can do multiple inheritance using , ..
    @abstractmethod
    def fly():
        pass

class Pigeon(Bird):    # example of multi level inheritance.. # level 2 inheritance  
    
    def sound(self):
        print("gutur gu.. gutur gu...")

    def fly(self):
        print("Flying.....")

p = Pigeon()
p.sound()
p.fly()





