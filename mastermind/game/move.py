class Move:
    """The Move class. The responsibility of it is to keep track of the players.
    Stereotypy:
        Information Holder
    Attributes:
        _code (int): Code to be guessed.
    """
    def __init__(self, code):
        """The class constructor.
        Args:
            self (Board): an instance of Board.
        """
        self._code = code

    def get_code(self):
        """Returns the code to be guessed.
        Args:
            self (Guess): an instance of Guess.
        """
        return self._code