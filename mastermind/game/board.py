import random 

class Board:

   def __init__(self):
        self.code = ""
        self._prepare
        self.guess = 0
      

   def apply(self, move):
        self.guess = move.get_code()
        
   

   def to_string(self):
      text = ""
      string_guess = str(self.guess)
      for i, digit in enumerate(self.code):
         if digit == string_guess[i]: text += ("X")
         elif digit in string_guess[i]: text += ("O")
         else:
            text += ("*")
      return(text)

         



   def _prepare(self):
        random_number = random.randint(1000, 9999)
        self.code = str(random_number)

# code = Board()
# code._prepare()
        




