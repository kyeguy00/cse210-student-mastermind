from game.player import Player
import random 


class Board:
     """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder
    Attributes:
        code(str): to return a random number between 1000 and 9999.
    """
    

     def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self.code = ""
        self._prepare()
        self.guess = 0
      

     def apply(self, move):
          """Applies the given move to the playing surface. In this case, it gets code from the player.
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """
          self.guess = move.get_code()
          

     def _prepare(self):
          """Sets up the board with a random number that the player need to guess.
        
        Args:
            self (Board): an instance of Board.
        """
          random_number = random.randint(1000, 9999)
          self.code = str(random_number)


