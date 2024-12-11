import puppy_state

class StatePlay(puppy_state.PuppyState):
    """Represents the playing state of the puppy."""
    
    def feed(self, puppy):
        return "The puppy is too busy playing with the ball to eat right now."
    
    def play(self, puppy):
        puppy.inc_plays()
        if puppy.plays >= 3:
            puppy.change_state("asleep")
            puppy.reset()
            return "The puppy played so much it fell asleep!"
        return "You throw the ball again and the puppy excitedly chases it."
