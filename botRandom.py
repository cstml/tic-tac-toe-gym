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
        self.game = _gameBeingPlayed
        self.character = _charcter
        
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
        print("I Lost")

    def nextMoveDecision(self):
        """
        Random bots takes a random position from 1 to 9 and tries to play it 
        """
        b = random.randint(1, 9) 
        while (self.Occupied(b)):
            b = random.randint(1, 9) 
        return b

    def Occupied(self,position):
        if (self.game.board[position] != self.game.neutralCharacter):
            print ("DUD")
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
