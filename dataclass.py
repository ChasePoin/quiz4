from dataclasses import dataclass

@dataclass
class Hero:
    health: int
    element: str
    weapon: str
    def currentStatus(self):        # display ALL object data
        print(f"Your hero is at {self.health} health, is well-versed in {self.element} and is powerfully wielding a {self.weapon}!")




# if __name__ == "__main__":
#     steven = Hero(100, "fire", "sword")
#     steven.currentStatus()