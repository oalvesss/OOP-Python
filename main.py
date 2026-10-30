from models.restautant import Restaurant

praca_restaurant = Restaurant(name="Da Praça", category="Gourmet")
requinte_restaurant = Restaurant(name="Requinte", category="Buffet")
teixeira_restaurant = Restaurant(name="Teixeira", category="Caseira")
# praca_restaurant.claimAssessment("Zé", 10)
teixeira_restaurant.claimAssessment("Lorena", 6)
requinte_restaurant.claimAssessment("Pedro", 9)
requinte_restaurant.claimAssessment("Graci", 3)


teixeira_restaurant.toggle_state()

def main():
    Restaurant.restaurants_list()

if __name__ == '__main__':
    main()