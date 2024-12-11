import abc

class PuppyState(abc.ABC):
    """
    PuppyState – interface
        a. feed(self, puppy) – abstract (no code)
        b. play(self, puppy) – abstract (no code)
    """
    @abc.abstractmethod
    def feed(self, puppy):
        """
        Defines the behavior when the puppy is fed.

        Args:
            puppy: The Puppy object.

        Returns:
            A string describing the reaction.
        """
        pass

    @abc.abstractmethod
    def play(self, puppy):
        """
        Defines the behavior when the puppy is played with.

        Args:
            puppy: The Puppy object.

        Returns:
            A string describing the reaction.
        """
        pass