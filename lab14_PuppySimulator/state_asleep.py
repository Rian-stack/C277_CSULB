import puppy_state

class StateAsleep(puppy_state.PuppyState):
    """
    Represents the asleep state of the puppy.
    """
    
    def feed(self, puppy):
        """
        Wakes the puppy up to eat.

        Args:
            puppy: The Puppy object.

        Returns:
            A string describing the reaction.
        """
        puppy.change_state("eating")
        puppy.reset()
        return "The puppy wakes up and comes running to eat."
    
    def play(self, puppy):
        """
        The puppy continues to sleep if played with.

        Args:
            puppy: The Puppy object.

        Returns:
            A string describing the reaction.
        """
        return "The puppy is asleep. It doesn't want to play right now."
    
    
