from models.restautant import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish


praca_restaurant = Restaurant(name="Da Praça", category="Gourmet")
requinte_restaurant = Restaurant(name="Requinte", category="Buffet")
teixeira_restaurant = Restaurant(name="Teixeira", category="Caseira")

drink_juice = Drink(name="Orange Juice", price=8.00, size= "big")
vinagret_dish = Dish(name= "Small Vinagret", price= 10.00, description="Better vinagret in the city")
requinte_restaurant.add_in_menu(drink_juice)
requinte_restaurant.add_in_menu(vinagret_dish)
drink_juice.apply_discount()
vinagret_dish.apply_discount()

def main():
    requinte_restaurant.show_menu



if __name__ == '__main__':
    main()