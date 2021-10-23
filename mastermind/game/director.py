from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster





class Director:
    
    
    def __init__(self):
            """The class constructor.
            
            Args:
                self (Director): an instance of Director.
            """
            self._board = Board()
            self._console = Console()
            self._keep_playing = True
            self._move = 0
            self._roster = Roster()
           

    def start_game(self):
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        


    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        # get next player's move
        player = self._roster.get_current()
        both_players = self._roster.players
        self._console.write("--------------------")
        self._console.write(f"Player {both_players[0].get_name()}: {both_players[0].get_move()}, {both_players[0].get_result()} ")
        self._console.write(f"Player {both_players[1].get_name()}: {both_players[1].get_move()}, {both_players[1].get_result()} ")
        self._console.write("--------------------")
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number("What is your guess? ")
        move = Move(guess)
        player.set_move(move.get_code())
        self._board.apply(move)
        player.set_result(self._board.code)
        board = player.get_result()
        self._console.write(board)
        


    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        self._move = player.get_move()
        
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking their guess and updating where the correct numbers are and incorrect numbers are.

        Args:
            self (Director): An instance of Director.
        """
        if self._move == int(self._board.code):
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")


            self._keep_playing = False
        self._roster.next_player()

        # if self._board.is_empty():
        #     winner = self._roster.get_current()
        #     name = winner.get_name()
        #     print(f"\n{name} won!")
        #     self._keep_playing = False
        # self._roster.next_player()
