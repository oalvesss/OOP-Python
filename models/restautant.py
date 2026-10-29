class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.restaurants.append(self)

    def __str__(self): # = a to string in java 
        return f"Restaurant Name: {self.name} | Category: {self.category}"

    def restaurants_list():
        for restaurant in Restaurant.restaurants:
            print(f"Restaurant Name: {restaurant.name} | Category: {restaurant.category} | Active: {restaurant.active}")

praca_restaurant = Restaurant(name="Da Praça", category="Gourmet")
requinte_restaurant = Restaurant(name="Requinte", category="Buffet")

# print(dir(praca_restaurant))  dir show atributes, metods this object
# print(vars(praca_restaurant))  vars show attribute dictionary

Restaurant.restaurants_list()