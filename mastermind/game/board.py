from game.player import Player
import random 


class Board:

   def __init__(self):

        self.code = ""
        self._prepare()
        self.guess = 0
      

   def apply(self, move):
        self.guess = move.get_code()


   def _prepare(self):
        random_number = random.randint(1000, 9999)
        self.code = str(random_number)


# code = Board()
# code._prepare()
        




