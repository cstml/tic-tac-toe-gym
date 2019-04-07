"""
The classic tic tac toe game

"""
import random

class TicTacToe(object):

    def __init__(self):
        """
        Initialise the board
        """
        self.board = ["a" for _ in range(10)]
        self.player = ["player 1","player2"]

    def GetPlayerName(self,number):
        return self.player[number]

    def DisplayBoard(self):
        firstLine = self.board[1] + " " + self.board[2] + " " + self.board[3]
        secondLine = self.board[4] + " " + self.board[5] + " " + self.board[6]
        thirdLine = self.board[7] + " " + self.board[8] + " " + self.board[9]
        print (firstLine)
        print (secondLine)
        print (thirdLine)
        return

if __name__ == "__main__":
    game = TicTacToe()
    print (game.GetPlayerName(1))
    game.DisplayBoard()
