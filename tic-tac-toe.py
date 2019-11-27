"""
The classic tic tac toe game
"""
import random
from botRandom import playerRandom
from humanPlayer import humanPlayer
from inteligentBot import inteligentBot as playerInteligent
from scoreboard import ScoreBoard

class TicTacToe(object):

    def __init__(self,championship):
        """ 
        Initialise the board
        """
        self.neutralCharacter = "-"
        self.xCharacter = "X"
        self.oCharacter = "O"
        self.board = [self.neutralCharacter for _ in range(10)]

        print ("Play against 1 for Random 2 for AI 3 for Inteligent")
        choice = input()

        if choice == 1:
            self.player1 = playerRandom(self,self.xCharacter)
        elif choice == 2:
            self.player1 = humanPlayer(self,self.xCharacter)
            self.player1.name = "human"
        elif choice == 3:
            self.player1 = playerInteligent(self,self.xCharacter)
            self.player1.name = "inteligent"

        print ("Play against: 1 for Random 2 for Human 3 for Inteligent")
        choice = input()

        if choice == 1:
            self.player2 = playerRandom(self,self.oCharacter)
            self.player1.name = "random"
        elif choice == 2:
            self.player2 = humanPlayer(self,self.oCharacter)
        elif choice == 3:
            self.player2 = playerInteligent(self,self.oCharacter)

        self.player = {"x" : self.player1,"y" : self.player2}

        self.winsPlayer1 = 0
        self.winsPlayer2 = 0
        self.numberOfGamesPlayed = 1
        self.numberOfGamesToPlay = input()
        self.numberOfMoves = 0

        self.scoreBoard = ScoreBoard(self,championship)

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

    def Win(self):
        board = self.board

        if ( board[1]==board[2]==board[3]!=self.neutralCharacter ):
            return True
        elif (board[4]==board[5]==board[6]!=self.neutralCharacter):
            return True
        elif (board[7]==board[8]==board[9]!=self.neutralCharacter):
            return True

        elif (board[1]==board[4]==board[7]!=self.neutralCharacter):
            return True
        elif (board[2]==board[5]==board[8]!=self.neutralCharacter):
            return True
        elif (board[3]==board[6]==board[9]!=self.neutralCharacter):
            return True

        elif (board[1]==board[5]==board[9]!=self.neutralCharacter):
            return True
        elif (board[3]==board[5]==board[7]!=self.neutralCharacter):
            return True

        return False

    def PlayerWin (self,winningPlayer):
        """
        Method that defines what happens when a player wins
        """
        if ( winningPlayer == 1):
            self.player1.Win()
            self.scoreBoard.winX()
            self.player2.Lose()

        if ( winningPlayer == 2):
            self.player1.Lose()
            self.player2.Win()
            self.scoreBoard.winY()

        if ( winningPlayer == 3):
            self.player1.Draw()
            self.player2.Draw()
            self.scoreBoard.Draw()

    def Draw(self):
        """
        Method defining what happens if the game ends in a draw 
        """
        if ( self.numberOfMoves == 8 ):
            return True
        else:
            return False

    def EraseBoard(self):
        """
        Initialise the board
        """
        self.board = [self.neutralCharacter for _ in range(10)]

    def Championship(self):
        print ("="*10)
        print ("Start of a new Championship set")
        print ("="*10)
        while (self.numberOfGamesPlayed <= self.numberOfGamesToPlay):
            self.EraseBoard()
            self.scoreBoard.newGame()
            print ("\n")
            print ("-" * 20)
            print ("Championship number: " + str(self.numberOfGamesPlayed))
            self.PlayGame()
            self.numberOfGamesPlayed += 1
            print ("\n")
        self.scoreBoard.printBoard()

    def AnalyzeBoard(self,playerTurn):
        if ( playerTurn == self.player1 ):
            if (self.Win()):
                return 1
            elif (self.Draw()):
                return 3
            else:
                return 0

        elif (playerTurn == self.player2):
            if (self.Win()):
                return 2
            elif (self.Draw()):
                return 3
            else:
                return 0

    def PlayGame(self):
        self.numberOfMoves = 0
        self.EraseBoard()
        playerTurn = self.player1

        while (self.numberOfMoves < 9):
            # Print number of current move
            print ("--Move " +str(self.numberOfMoves))

            playerTurn.Move() # calls player to make a move

            # Display board
            self.DisplayBoard()

            # Analyze board
            result = self.AnalyzeBoard(playerTurn)
            if (result == 1):
                self.PlayerWin(1)
                return
            elif (result == 2):
                self.PlayerWin(2)
                return
            elif (result == 3):
                self.PlayerWin(3)
                return

            # next player
            if (playerTurn == self.player1):
                playerTurn = self.player2
            elif (playerTurn == self.player2):
                playerTurn = self.player1
            self.numberOfMoves += 1


if __name__ == "__main__":
    game = TicTacToe(1)
    game.DisplayBoard()
    game.Championship()

