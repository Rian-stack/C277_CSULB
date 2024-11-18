import plate

class Small_Plate(plate.Plate):
    def description(self):
        '''returns the description of the plate'''
        return self.description
    
    def area(self):
        '''returns the area of the plate, the small plate can hold 78'''
        return 78
    
    def weight(self):
        '''returns the weight capcity of the plate, the small plate can hold 32'''
        return 32
    
    def count(self):
        '''returns 0, no items on the plate yet'''
        return 0