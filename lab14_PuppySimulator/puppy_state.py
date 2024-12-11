import abc

class PuppyState(abc.ABC):
    '''
    PuppyState – interface
        a. feed(self, puppy) – abstract (no code)
        b. play(self, puppy) – abstract (no code)
    '''
    @abc.abstractmethod
    def feed(self, puppy):
        pass

    @abc.abstractmethod
    def play(self, puppy):
        pass