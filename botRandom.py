"""
The random player 
always chooses a random move
"""
import random

class playerRandom(object):
    
    def __init__(self, _gameBeingPlayed, _charcter):
        """
        Initialise each bot with their character and the game they are part of
        """
        self.name = "random"
        random.seed(2)
        self.game = _gameBeingPlayed
        self.character = _charcter
        self.neutralCharacter = self.game.neutralCharacter
        
    def Win(self):
        """
        Method that the bot does when it looses
        """
        print ( 10*"*")
        print ("Player " + self.character + " says:")
        print ("I Won")
        print ( 10*"*")

    def Lose(self):
        """
        Method that the bot does when it loses
        """
        print ( 10*"*")
        print ("Player " + self.character + " says:")
        print ("I Lost")
        print ( 10*"*")

    def Draw(self):
        """
        Method that the bot does when it draws
        """
        print ( 10*"*")
        print ("Player " + self.character + " says:")
        print ("It's a Draw")
        print ( 10*"*")


    def nextMoveDecision(self):
        """
        Random bots takes a random position from 1 to 9 and tries to play it 
        """
        b = random.randint(1, 9) 
        while (self.Occupied(b)):
            b = random.randint(1, 9) 
        return b

    def Occupied(self,position):
        if (self.game.board[position] != self.neutralCharacter):
            """ Debug
            print (position)
            print (self.game.board)
            print ("DUD")
            """
            return True
        else:
            return False

    def Move(self):
        nextMoveDecisionPosition = self.nextMoveDecision()
        self.Tick(nextMoveDecisionPosition)
        return

    def Tick(self, position):
        self.game.board[position] = self.character
        return


if __name__ == "__main__":
    player = playerRandom()
    print (player.move())
