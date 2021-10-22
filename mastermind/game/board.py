import random 

class Board:

     def __init__(self):
        self.code = 0
        self._prepare
        
        

     def apply(self, move):
        guess = move.get_guess()
    
     def _prepare(self):
        self.code = random.randint(1000, 9999)
        print(self.code)

code = Board()
code._prepare()
        




