class Restaurant:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False

raca_restaurant = Restaurant(name="Da Praça", category="Gourmet")
requinte_restaurant = Restaurant(name="Requinte", category="Buffet")

print(vars(raca_restaurant))
print(vars(requinte_restaurant))

