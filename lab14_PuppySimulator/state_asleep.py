import puppy_state

class StateAsleep(puppy_state.PuppyState):
    """Represents the asleep state of the puppy."""
    
    def feed(self, puppy):
        puppy.change_state("eating")
        puppy.reset()
        return "The puppy wakes up and comes running to eat."
    
    def play(self, puppy):
        return "The puppy is asleep. It doesn't want to play right now."
    
    
