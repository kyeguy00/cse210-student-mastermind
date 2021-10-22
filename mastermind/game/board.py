from game.player import Player
import random 


class Board:

   def __init__(self):
      self.code = 0
      self.prepare
      self._items = {}
      #self.player = Player()

        
        

   # def apply(self, move):
   #    guess = move.get_guess()
    
   # def _prepare(self):
   #    self.code = random.randint(1000, 9999)
   #    print(self.code)

   

   def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]
        
   def _create_hint(self, code, guess):
      """Generates a hint based on the given code and guess.

      Args:
         self (Board): An instance of Board.
         code (string): The code to compare with.
         guess (string): The guess that was made.

      Returns:
         string: A hint in the form [xxxx]
      """ 
      hint = ""
      for index, letter in enumerate(guess):
         if code[index] == letter:
               hint += "x"
         elif letter in code:
               hint += "o"
         else:
               hint += "*"
      return hint
   
   def to_string(self):
      """Converts the board data to its string representation.
      Args:
         self (Board): an instance of Board.
      Returns:
         string: A representation of the current board.
      """ 
      text = "\n--------------------"

      text += (f"\nPlayer {self._items}")
      text += (f"\nPlayer {self._items}")

      text = "\n--------------------"

      return text

      

# code = Board()
# code._prepare()
        




