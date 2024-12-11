import state_asleep
import state_eat
import state_play

class Puppy:
    """
    Puppy – the object that the user interacts with.
        a. Attributes: _state, _feeds, _plays – add properties for feed and plays.
        b. __init__(self) – initializes the state to the asleep state, and then initializes the
        number of feeds and plays.
        c. properties for feed and plays.
        d. change_state(self, new_state) – updates the puppy’s state to the new state.
        e. throw_ball(self) – calls the play method for whichever state the puppy is in.
        f. give_food(self) – calls the feed method for whichever state the puppy is in.
        g. inc_feeds(self) – increments the number of times the puppy has been fed in a row.
        h. inc_plays(self) – increments the number of times the puppy has played in a row.
        i. reset(self) – reinitializes the feeds and plays attributes.
    """
    
    def __init__(self, name):
        """
        Initializes the puppy object.
        """
        self.name = name
        self._state = state_asleep.StateAsleep()
        self._feeds = 0
        self._plays = 0
    
    @property
    def feeds(self):
        """
        Returns the number of consecutive feeds.
        """
        return self._feeds
    
    @property
    def plays(self):
        """
        Returns the number of consecutive plays.
        """
        return self._plays
    
    def change_state(self, new_state):
        """
        Changes the puppy's current state.

        Args:
            new_state: The new state object to set.
        """
        if new_state == "asleep":
            self._state = state_asleep.StateAsleep()
        elif new_state == "eating":
            self._state = state_eat.StateEat()
        elif new_state == "playing":
            self._state = state_play.StatePlay()
    
    def throw_ball(self):
        """
        Interacts with the current state to play with the puppy.
        Returns:
            A string describing the puppy's reaction.
        """
        return self._state.play(self)
    
    def give_food(self):
        """
        Interacts with the current state to feed the puppy.
        Returns:
            A string describing the puppy's reaction.
        """
        return self._state.feed(self)
    
    def inc_feeds(self):
        """
        Increments the feed counter.
        """
        self._feeds += 1
    
    def inc_plays(self):
        """
        Increments the play counter.
        """
        self._plays += 1
    
    def reset(self):
        """
        Resets the feed and play counters.
        """
        self._feeds = 0
        self._plays = 0