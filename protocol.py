from typing import Protocol

class Animal(Protocol):
    def __init__(self):
        pass

    def meow(self):
        pass
    
    def roar(self):
        pass

class Cat:
    def __init__(self):
        pass

    def meow(self):
        print("MEOW!")

class Tiger:
    def __init__(self):
        pass

    def meow(self):
        print("MEOOOOOOOOOW!")

    def roar(self):
        print("RAAAAAAAAAAAAAH!")