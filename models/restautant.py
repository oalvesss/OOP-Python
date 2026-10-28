class Restaurant:
    name = ""
    category = ""
    active = False

praca_restaurant = Restaurant()
praca_restaurant.name = "Da Praça"
praca_restaurant.category = "Gourmet"

requinte_restaurant = Restaurant()

restaurants = [praca_restaurant, requinte_restaurant]

# print(dir(praca_restaurant))  dir show atributes, metods this object

print(vars(praca_restaurant)) # vars show attribute dictionary
