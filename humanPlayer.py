"""
The human player class
"""

class humanPlayer(object):

    def __init__(self,game,character):
        print ("Hello Human Player")

        self.name = "human"
        self.game=game
        self.character=character

    def Win(self):
        print (" PC is stoopid")

    def Draw(self):
        print ("Draw")

    def Lose(self):
        print ("hooman is dumb")

    def PositionsAvailable(self):
        listOfPositions=[]
        for a in range(1,10):
            if self.game.board[a] == self.game.neutralCharacter :
                listOfPositions.append(a)
        return listOfPositions
            

    def Move(self):
        print ("where do you want to tick")
        p = self.PositionsAvailable()
        print (p)
        move = input()
        if move in p:
            self.Tick(move)
        else:
            self.Move()

    def Tick(self,position):
        self.game.board[position]=self.character
        return

