class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last move.
    
    Stereotype: 
        Information Holder
    Attributes:
        _name (string): The player's name.
        _move (Move): The player's last move.
    """
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._move = "----"
        self._result = "****"
        
        
    def get_guess(self):
        """Returns the player's last move (an instance of Move). If the player 
        hasn't moved yet this method returns None.
        Args:
            self (Player): an instance of Player.
        """
        return self._move

    def get_name(self):
        """Returns the player's name.
        Args:
            self (Player): an instance of Player.
        """
        return self._name.capitalize()

    def set_move(self, move):
        """Sets the player's last move to the given instance of Move.
        Args:
            self (Player): an instance of Player.
            move (Move): an instance of Move
        """
        self._move = move

    def get_result(self):
        return(self._result)


    def set_result(self, code):
        text = ""
        string_guess = str(self._move)
        for i, digit in enumerate(code):
            if digit == string_guess[i]: text += ("X")
            elif digit in string_guess: text += ("O")
            else:
                text += ("*")
        self._result = text
        return(self._result)