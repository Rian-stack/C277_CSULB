import plate
class SmallPlate(plate.Plate):
    """
    class represent small plate, inherit from abstract base class Plate
    """
    
    def description(self):
        '''returns the description of the plate'''
        return "Small plate "   
        
    def area(self):
        '''returns the area of the plate, the small plate can hold 78'''
        return 78

    def weight(self):
        '''returns the weight capcity of the plate, the small plate can hold 32'''
        return 32

    def count(self):
        '''returns the number of food items on the plate'''
        return 0