from models.restautant import Restaurant

praca_restaurant = Restaurant(name="Da Praça", category="Gourmet")
requinte_restaurant = Restaurant(name="Requinte", category="Buffet")
teixeira_restaurant = Restaurant(name="Teixeira", category="Caseira")

teixeira_restaurant.toggle_state()

def main():
    Restaurant.restaurants_list()

if __name__ == '__main__':
    main()