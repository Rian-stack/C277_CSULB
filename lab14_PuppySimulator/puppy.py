import state_asleep
import state_eat
import state_play


class Puppy:
    """Represents the puppy object."""
    
    def __init__(self, name):
        self.name = name
        self._state = state_asleep.StateAsleep()
        self._feeds = 0
        self._plays = 0
    
    @property
    def feeds(self):
        return self._feeds
    
    @property
    def plays(self):
        return self._plays
    
    def change_state(self, new_state):
        """Change the puppy's state."""
        if new_state == "asleep":
            self._state = state_asleep.StateAsleep()
        elif new_state == "eating":
            self._state = state_eat.StateEat()
        elif new_state == "playing":
            self._state = state_play.StatePlay()
    
    def throw_ball(self):
        return self._state.play(self)
    
    def give_food(self):
        return self._state.feed(self)
    
    def inc_feeds(self):
        self._feeds += 1
    
    def inc_plays(self):
        self._plays += 1
    
    def reset(self):
        self._feeds = 0
        self._plays = 0