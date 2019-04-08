"""
The random player 
always chooses a random move
"""
import random

class playerRandom(object):
    
    def __init__(self, _gameBeingPlayed, _charcter):
        self.game = _gameBeingPlayed
        self.character = _charcter
        
    def Win(self):
        print("I Won")

    def nextMove(self):
        b = random.randint(1, 9) 
        return b

    def Occupied(self,position):
        if (self.game.board[position] != self.game.neutralCharacter):
            print ("DUD")
            return False
        else:
            return True

    def Move(self):
        nextMovePosition = self.nextMove()
        self.Tick(nextMovePosition)
        return

    def Tick(self, position):
        self.game.board[position] = self.character
        return


if __name__ == "__main__":
    player = playerRandom()
    print (player.move())
