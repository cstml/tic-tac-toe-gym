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
        self.xCharacter = "X"
        self.oCharacter = "O"
        self.board = [self.neutralCharacter for _ in range(10)]
        self.boardAvailable = [self.neutralCharacter for _ in range(10)]
        self.player1 = playerRandom(self,self.xCharacter)
        self.player2 = playerRandom(self,self.oCharacter)
        self.player = {"x" : self.player1,"y" : self.player2}

        self.winsPlayer1 = 0
        self.winsPlayer2 = 0
        self.numberOfGamesPlayed = 1
        self.numberOfGamesToPlay = 2
        self.numberOfMoves = 0

    def DisplayBoard(self):
        """
        Method that displays the board 
        """
        firstLine = self.board[1] + " " + self.board[2] + " " + self.board[3]
        secondLine = self.board[4] + " " + self.board[5] + " " + self.board[6]
        thirdLine = self.board[7] + " " + self.board[8] + " " + self.board[9]
        print (firstLine)
        print (secondLine)
        print (thirdLine)
        return

    def Win(self,playerTurn):
        board = self.board
        if ( board[1] == board[2] == board[3] != self.neutralCharacter ):
            playerTurn.Win()
            return True
        elif (board[4]==board[5]==board[6]!=self.neutralCharacter):
            self.ScoreBoardWinItterate(playerTurn)
            playerTurn.Win()
            return True
        elif (board[7]==board[8]==board[9]!=self.neutralCharacter):
            self.ScoreBoardWinItterate(playerTurn)
            playerTurn.Win()
            return True
        elif (board[1]==board[4]==board[7]!=self.neutralCharacter):
            self.ScoreBoardWinItterate(playerTurn)
            playerTurn.Win()
            return True
        elif (board[2]==board[6]==board[8]!=self.neutralCharacter):
            self.ScoreBoardWinItterate(playerTurn)
            playerTurn.Win()
            return True
        elif (board[3]==board[6]==board[9]!=self.neutralCharacter):
            self.ScoreBoardWinItterate(playerTurn)
            playerTurn.Win()
            return True
        return False

    def PlayerWin (self,playerTurn):
        """
        Method that defines what happens when a player wins
        """
        if ( playerTurn.character == self.xCharacter )
            self.ScoreBoardWinItterate(playerTurn)

        if ( playerTurn.character == self.yCharacter )
            self.ScoreBoardWinItterate(playerTurn)

    def Draw(self):
        """
        Method defining what happens if the game ends in a draw 
        """
        if ( self.numberOfMoves == 10 ):
            print ("Draw")
            return True
        else:
            return False

    def EraseBoard(self):
        self.DisplayBoard()
        self.board = [self.neutralCharacter for _ in range(10)]

    def Championship(self):
        print ("Start of a new Championship set")
        while (self.numberOfGamesPlayed <= self.numberOfGamesToPlay):
            print ("-Championship number " + str(self.numberOfGamesPlayed))
            self.PlayGame()
            self.numberOfGamesPlayed += 1
            self.EraseBoard()

    def AnalyzeBoard(self,playerTurn):
        if ( playerTurn == 1 ):
            if (self.Win()):
                return 1
            elif (self.Draw()):
                return 3
            elif:
                return 0
        elif (playerTurn == 2):
            if (self.Win()):
                return 2
            elif (self.Draw()):
                return 3
            elif:
                return 0

    def PlayGame(self):
        self.numberOfMoves = 0
        self.EraseBoard()
        playerTurn = self.player1

        while (self.numberOfMoves < 10):
            print ("--Move " +str(self.numberOfMoves))
            playerTurn.move()
                # calls player to make a move
            result = AnalyzeBoard()
            if (result == 1):
                player1wins()
            elif (result == 2):
                player2wins()
            elif (result == 3):
                itsadraw()

            #nextplayer()
            if playerTurn == self.player1):
                playerTurn = self.player2
                # next player
                # moves++
            self.player1.Move()
            self.DisplayBoard()
            self.numberOfMoves+=1
            if (self.AnalyzeBoard(self.player1)):
                return

            print ("--Move " +str(self.numberOfMoves))
            self.player2.Move()
            self.DisplayBoard()
            self.numberOfMoves+=1
            if (self.AnalyzeBoard(self.player2)):
                return

if __name__ == "__main__":
    game = TicTacToe()
    game.DisplayBoard()
    game.Championship()

