import puppy_state

class StateEat(puppy_state.PuppyState):
    """Represents the eating state of the puppy."""
    
    def feed(self, puppy):
        puppy.inc_feeds()
        if puppy.feeds >= 3:
            puppy.change_state("asleep")
            puppy.reset()
            return "The puppy ate so much it fell asleep!"
        return "The puppy continues to eat as you add another scoop of kibble to its bowl."
    
    def play(self, puppy):
        puppy.change_state("playing")
        puppy.reset()
        return "The puppy looks up from its food and chases the ball you threw."
