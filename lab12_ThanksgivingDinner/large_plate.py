import plate

class Large_Plate(plate.Plate):
    '''extends plate'''
    def description(self):
        '''returns the description of the plate and the food on it.'''
        food_descriptions = ''
        return f"A large plate with: " + food_descriptions

    def area(self):
        '''returns the area of the plate, the small plate can hold 113'''
        return 113
    
    def weight(self):
        '''returns the weight capcity of the plate, the small plate can hold 24'''
        return 24
    
    def count(self):
        '''returns the number of food items on the plate'''
        return 0