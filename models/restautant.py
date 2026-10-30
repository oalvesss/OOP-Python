from models.assessment import Assessment
class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False # _ == private
        self._assessment = []
        Restaurant.restaurants.append(self)

    def __str__(self): # = a to string in java 
        return f"Restaurant Name: {self._name} | Category: {self._category}"
    
    @classmethod
    def restaurants_list(cls):
        for restaurant in cls.restaurants:
            print(f"Restaurant Name: {restaurant._name.ljust(10)} | Category: {restaurant._category.ljust(10)} | Active: {restaurant.active}")

    @property 
    def active(self):
        return "✅" if self._active else "❌"

    def toggle_state(self):
        self._active = not self._active

    