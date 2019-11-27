"""
The inteligent BOT
Based on information from
https://medium.com/@hadican/how-to-build-a-simple-artificial-neural-network-ann-a064939f940b
https://towardsdatascience.com/first-neural-network-for-beginners-explained-with-code-4cfd37e06eaf
https://skymind.ai/wiki/neural-network ****
"""

from numpy import exp, array, random, dot
import numpy as np
import pickle



class inteligentBot():

    def __init__(self, _gameBeingPlayed, _character):
        self.game = _gameBeingPlayed
        self.name = "inteligent"
        self.character = _character
        self.state = []
        self.state_value = {}
        self.loadPolicy()
        self.neutralCharacter = self.game.neutralCharacter
        self.moves = []
        self.decayGamma=0.9
        self.learnRate=0.2
        

    def Read(self):
        """
        Checks where the player can make a move
        """
        board = self.game.board
        availablePosition = []
        for a in range(1,10):
            if (self.game.board[a] is self.game.neutralCharacter):
                availablePosition.append(a)
        return availablePosition


    def Move(self):
        potentialMove = self.Read()
        curentMax = -9999
        print (potentialMove)
        if (np.random.uniform(1,10) < 2):
            curentMove = potentialMove[int(np.random.randint(0,(len(potentialMove))))]
            print ("Random")
        else:
            for move in potentialMove :
                nextBoard=list(self.game.board)
                nextBoard[move]=self.character
                nextBoardHash= str(nextBoard)
                if self.state_value.get(nextBoardHash) is None:
                    self.state_value[nextBoardHash] = 0
                    potentialValue = 0.00
                else:
                    potentialValue = self.state_value[nextBoardHash]
                
                if potentialValue >= curentMax:
                    curentMax = potentialValue
                    curentMove = move

        print("Will move at "+str(curentMove))
        print("Due to value of "+str(curentMax))

        self.game.board[curentMove] = self.character

        curentMoveHash=str(self.game.board)
        self.moves.append(curentMoveHash)

        return 0

    def Backfeed(self,reward):
        for moveHash in reversed(self.moves): 
            if self.state_value.get(moveHash) is None:
                self.state_value[moveHash] = 0.0
            self.state_value[moveHash]+= self.learnRate * (self.decayGamma * reward - self.state_value[moveHash])
            reward = self.state_value[moveHash]


    def Win(self):
        print("Inteligent won")
        self.Backfeed(1)
        self.savePolicy()

    def Lose(self):
        print("Inteligent lost")
        self.Backfeed(0)
        self.savePolicy()

    def Draw(self):
        print("It's a draw!")
        self.Backfeed(0.2)
        self.savePolicy()

    def reset(self):
        self.state = []

    def savePolicy(self):
        fw = open('policy_' + str(self.character), 'wb')
        pickle.dump(self.state_value, fw)
        fw.close()

    def loadPolicy(self):
        file = 'policy_' + str(self.character)
        fr = open(file, 'rb')
        self.state_value = pickle.load(fr)
        fr.close()


if __name__ == "__main__":
    test = neuroNetwork()
    test.debug(1)
