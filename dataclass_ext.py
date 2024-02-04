from dataclasses import dataclass
import random as r

@dataclass
class Hero:
    health: int
    element: str
    weapon: str
    def currentStatus(self):            # display ALL object data
        print(f"Your hero is at {self.health} health, is well-versed in {self.element} and is powerfully wielding a {self.weapon}!")

    def damageHero(self):               # manipulate health
        damage = r.randrange(0,100)
        self.health = self.health - damage
        if(damage <= 65):
            print(f"Hero damaged! Health is now at {self.health}!")
        else:
            print(f"Critical hit! Health is now at {self.health}!")




# if __name__ == "__main__":
#     steven = Hero(100, "fire", "sword")
#     steven.currentStatus()
#     steven.damageHero()
#     steven.currentStatus()