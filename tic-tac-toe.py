"""
The classic tic tac toe game
"""
import random
from botRandom import playerRandom

class TicTacToe(object):

    def __init__(self):
        """ 
        Initialise the board
        """
        self.neutralCharacter = "-"
        self.board = [self.neutralCharacter for _ in range(10)]
        self.boardAvailable = [self.neutralCharacter for _ in range(10)]
        self.player1 = playerRandom(self,"x")
        self.player2 = playerRandom(self,"o")
        self.player = {"x" : self.player1,"y" : self.player2}

        self.winsPlayer1 = 0
        self.winsPlayer2 = 0
        self.numberOfGamesPlayed = 1
        self.numberOfGamesToPlay = 2
        self.numberOfMoves = 0

    def DisplayBoard(self):
        firstLine = self.board[1] + " " + self.board[2] + " " + self.board[3]
        secondLine = self.board[4] + " " + self.board[5] + " " + self.board[6]
        thirdLine = self.board[7] + " " + self.board[8] + " " + self.board[9]
        print (firstLine)
        print (secondLine)
        print (thirdLine)
        return

    def Win(self):
        board = self.board
        if ( board[1] == board[2] == board[3] != self.neutralCharacter ):
            self.player[board[1]].Win()
            return True
        elif (board[4]==board[5]==board[6]!=self.neutralCharacter):
            self.player[board[4]].Win()
            return True
        elif (board[7]==board[8]==board[9]!=self.neutralCharacter):
            self.player[board[7]].Win()
            return True
        elif (board[1]==board[4]==board[7]!=self.neutralCharacter):
            self.player[board[4]].Win()
            return True
        elif (board[2]==board[6]==board[8]!=self.neutralCharacter):
            self.player[board[2]].Win()
            return True
        elif (board[3]==board[6]==board[9]!=self.neutralCharacter):
            self.player[board[3]].Win()
            return True
        return False

    def Draw(self):
        if self.numberOfMoves == 9:
            print ("Draw")
            return "Draw"
        else:
            return False

    def EraseBoard(self):
        self.DisplayBoard()
        self.board = [self.neutralCharacter for _ in range(10)]


    def Championship(self):
        while (self.numberOfGamesPlayed <= self.numberOfGamesToPlay):
            print ("Championship number " + str(self.numberOfGamesPlayed))
            self.PlayGame()
            self.numberOfGamesPlayed += 1
            self.EraseBoard()

    def AnalyzeBoard(self):
        if (self.Win()):
            print ("Win")
            return "Win"
        if (self.Draw()):
            print ("Draw")
            return "Draw"
        return False

    def PlayGame(self):
        self.numberOfMoves = 0
        while (self.numberOfMoves < 10):
            self.player1.Move()
            self.numberOfMoves+=1
            if (self.AnalyzeBoard()):
                return

            self.player2.Move()
            self.numberOfMoves+=1
            if (self.AnalyzeBoard()):
                return

if __name__ == "__main__":
    game = TicTacToe()
    game.DisplayBoard()
    game.Championship()

