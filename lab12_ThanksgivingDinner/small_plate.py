import plate

class Small_Plate(plate.Plate):
    def __init__(self):
        self._food = []

    def description(self):
        '''returns the description of the plate and the food on it.'''
        if not self._food:
            return "A small plate with nothing on it."
        else:
            food_descriptions = [f.description() for f in self._food]
            return f"A small plate with: {', '.join(food_descriptions)}"

    def area(self):
        '''returns the area of the plate, the small plate can hold 78'''
        return 78
    
    def weight(self):
        '''returns the weight capcity of the plate, the small plate can hold 32'''
        return 32
    
    def count(self):
        '''returns the number of food items on the plate'''
        return len(self._food)
