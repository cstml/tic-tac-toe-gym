"""
Defines the scoreboard class of the game Tic Tac Toe
Which keeps track of which player won which game and 
championship
"""


class ScoreBoard(object):

    def __init__(self,championship):
        self.game = 0
        self.championshipNumber = championship
        self.xWins = 0
        self.yWins = 0 
        self.draws = 0

    def winX(self):
        self.xWins += 1
        self.newGame()
        return

    def winY(self):
        self.yWins += 1
        self.newGame()
        return

    def Draw(self):
        self.draws += 1
        self.newGame()

    def newGame(self):
        self.game += 1

    def printBoard(self):
        print ("=" * 20)
        print ("Scoreboard")
        print ("X : " + str(self.xWins) + " dumb")
        print ("0 : " + str(self.yWins) + " inteligent")
        print ("Draw : " + str(self.draws))
        print ("=" * 20)

