class Restaurant:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False

    def __str__(self):
        return f"Name: {self.name} | Category: {self.category}"

raca_restaurant = Restaurant(name="Da Praça", category="Gourmet")
requinte_restaurant = Restaurant(name="Requinte", category="Buffet")

print(raca_restaurant)
print(requinte_restaurant)

