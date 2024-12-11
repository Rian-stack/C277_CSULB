class Puppy:
    '''
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
    '''
    def __init__(self):
        self._state = 'asleep'
        self._feeds = 0
        self._plays = 0
    
    @property
    def feed(self):
        return self._feeds
    
    @property
    def play(self):
        return self._plays
    
    def change_state(self, new_state):
        self._state = new_state

    def throw_ball(self):
        if self._state == 'asleep':
            return 'Zzzzzzzzzzz'
        elif self._state == 'awake':
            return 'Wagging tail'
        elif self._state == 'hungry':
            return 'Not interested'
        elif self._state == 'hungry and awake':
            return 'Not interested'
        elif self._state == 'hungry and tired':
            return 'Not interested'
        elif self._state == 'tired':
            return 'Not interested'
        elif self._state == 'tired and awake':
            return 'Not interested'
        elif self._state == 'tired and hungry':
            return 'Not interested'
        
    def give_food(self):
        if self._state == 'asleep':
            return 'Zzzzzzzzzzz'
        elif self._state == 'awake':
            return 'Yum yum yum'
        elif self._state == 'hungry':
            return 'Eating eagerly'
        elif self._state == 'hungry and awake':
            return 'Eating eagerly'
        elif self._state == 'hungry and tired':
            return 'Eating slowly'
        elif self._state == 'tired':
            return 'Not interested'
        elif self._state == 'tired and awake':
            return 'Not interested'
        elif self._state == 'tired and hungry':
            return 'Eating slowly'
        
    def inc_feeds(self):
        self._feeds += 1

    def inc_plays(self):
        self._plays += 1

    def reset(self):
        self._feeds = 0
        self._plays = 0

    

    