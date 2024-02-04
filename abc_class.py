from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def meow(self):
        pass

    @abstractmethod
    def roar(self):
        pass

class Cat(Animal):
    def __init__(self):
        pass

    def meow(self):
        print("MEOW!")

class Tiger(Animal):
    def __init__(self):
        pass

    def meow(self):
        print("MEOOOOOOOOOW!")

    def roar(self):
        print("RAAAAAAAAAAAAAH!")