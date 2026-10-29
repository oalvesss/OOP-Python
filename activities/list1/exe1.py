class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

car1 = Car(model="Polo", color="Black", year= 2003)
print(vars(car1))

