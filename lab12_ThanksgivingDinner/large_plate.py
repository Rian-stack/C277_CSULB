import plate

class LargePlate(plate.Plate):
    """
    class represent large plate, inherit from abstract base class Plate
    """

    def description(self):
        '''returns the description of the plate'''
        return "Large plate "

    def area(self):
        '''returns the area of the plate, the small plate can hold 113'''
        return 113

    def weight(self):
        '''returns the weight capcity of the plate, the small plate can hold 24'''
        return 24

    def count(self):
        '''returns the number of food items on the plate'''
        return 0