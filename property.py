class Food:
    def __init__(self, flavor: str, rating: int) -> None:
        self._flavor = flavor
        if ((rating >= 0) & (rating <= 5)):
            self._rating = rating
        else:
            print("Rating must be between 0 and 5 stars in order to be set.")        

    @property
    def flavor(self):
        return self._flavor
    
    @property
    def rating(self):
        return self._rating
    
    @flavor.setter
    def flavor(self, newFlavor: str):
        self._flavor = newFlavor    
    @rating.setter
    def rating(self, newRating: int):
        if ((newRating >= 0) & (newRating <= 5)):
            self._rating = newRating
        else:
            print("Rating must be between 0 and 5 stars.")

    def foodDescription(self):
        if (self._rating <= 2):
            print(f"Your food has a terrible {self._flavor} flavor and is rated poorly at {self._rating} stars.")            
        else:
            print(f"Your food has a very nice {self._flavor} flavor and is rated highly at {self._rating} stars!")
    
    
    
    

# if __name__ == "__main__":
#     steak = Food("savory", 4)
#     risotto = Food("sweet", 1)