"""
The random player 
always chooses a random move
"""
import random

class playerRandom(object):

    def move(self):
        self.b = random.randint(1, 9)
        return self.b

if __name__ == "__main__":
    player = playerRandom()
    print (player.move())
