import door
import random

class Basic_Door(door.Door):
    '''                                                                                                                                                                                      
     A basic door. You either push or pull                                                                                                                                                    
     '''                                                                                                                                                                                      
    def __init__(self):                                                                                                                                                                      
        self._solution = random.randint(1, 2)                                                                                                                                                
        self._input = None                                                                                                                                                                   
                                                                                                                                                                                            
    def examine_door(self):                                                                                                                                                                  
        return "A basic door. You can either push or pull it to open."                                                                                                                       
                                                                                                                                                                                            
    def menu_options(self):                                                                                                                                                                  
        return "1. Push\n2. Pull"                                                                                                                                                            
                                                                                                                                                                                            
    def get_menu_max(self):                                                                                                                                                                  
        return 2                                                                                                                                                                             
                                                                                                                                                                                            
    def attempt(self, option):                                                                                                                                                               
        self._input = option                                                                                                                                                                 
        return "" # Add description of attempt here                                                                                                                                          
                                                                                                                                                                                            
    def is_unlocked(self):                                                                                                                                                                   
        return self._input == self._solution                                                                                                                                                 
                                                                                                                                                                                            
    def clue(self):                                                                                                                                                                          
        return "Try the other way."                                                                                                                                                          
                                                                                                                                                                                            
    def success(self):                                                                                                                                                                       
        return "" # Add success message here    
