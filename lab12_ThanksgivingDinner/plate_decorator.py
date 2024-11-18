import abc
import plate

class Plate_Decorator(plate.Plate):
    '''
    PlateDecorator – extends ABC and extends from Plate
        a. __init__(self, p) – pass in the plate p and assign it to the _plate attribute.
        b. description, area, weight, count methods: call each on your _plate attribute
    '''
    def __init__(self, plate):
        self._plate = plate

    def description(self):
        return self._plate.description()

    def area(self):
        return self._plate.area()
    
    def weight(self):
        return self._plate.weight()

    def count(self):
        return self._plate.count()
