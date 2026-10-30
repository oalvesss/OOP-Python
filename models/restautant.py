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
            assessment = str(restaurant.assessmentNote).ljust(10)# para nao dar erro de tipo float com o ljust
            print(f"Restaurant Name: {restaurant._name.ljust(10)} | Category: {restaurant._category.ljust(10)} | Assessment: {assessment} | Active: {restaurant.active}")

    @property 
    def active(self):
        return "✅" if self._active else "❌"

    def toggle_state(self):
        self._active = not self._active

    def claimAssessment(self, client, note):
        if 0 < note <= 5:
            assessment = Assessment(client, note)
            self._assessment.append(assessment)

    @property
    def assessmentNote(self):
        if not self._assessment:
            return "No reviews"
        sum_notes = sum(assessment._note for assessment in self._assessment)
        amount_notes = len(self._assessment)
        average = round(sum_notes / amount_notes, 1)
        return average
        
    