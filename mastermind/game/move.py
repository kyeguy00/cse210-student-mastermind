class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder
    Attributes:
        _pile (integer): The pile to remove from.
        _stones (integer): The number of stones to remove.
    """
    def __init__(self, apply):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self.apply = apply
        #self._prepare = prepare

    def get_apply(self):
        """Returns the pile to remove from.
        Args:
            self (Move): an instance of Move.
        """
        return self.apply

    def get_random(self):
        """Returns the number of stones to remove.
        Args:
            self (Move): an instance of Move.
        """
        return self._prepare

    def last_move(self):
        """Save the last move made by the player

        Args:
            self (Move): an instance of Move
        """

