"""
The inteligent BOT
Based on information from
https://medium.com/@hadican/how-to-build-a-simple-artificial-neural-network-ann-a064939f940b
https://towardsdatascience.com/first-neural-network-for-beginners-explained-with-code-4cfd37e06eaf
https://skymind.ai/wiki/neural-network ****
"""

from numpy import exp, array, random, dot
import numpy as np

class neuroNetwork():
    def __init__(self):
        random.seed(1)
        # We model a single neuron, with 9 input connections and 9 output connection.
        # We assign random weights to a 9 x 1 matrix, with values in the range -1 to 1
        # and mean 0.
        self.input   = random.rand(10)*2
        self.synaptic_weights = random.rand(9, 9,9)*2-1 
        self.synaptic_weights = self.__sigmoid(self.synaptic_weights)
        self.synaptic_output  = random.rand(10)*2-1 

    def __sigmoid(self, x):
        """
        sigmoid function normalises the output of a neuron to a number between 0 and 1
        """
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def __think(self,inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

    def __train (self, training_inputs, training_outputs, number_of_iterations):
        for iteration in range(number_of_iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments

    def debug (self,input):
        """
        A function I use to test if the class is working
        """
        print (self.synaptic_weights)
        print (self.__sigmoid(self.synaptic_weights))
        print ()
        print (self.__sigmoid_derivative(self.synaptic_weights))
        print ()
        print (self.__sigmoid(input))
        print ()
        print (self.__sigmoid_derivative(input))

class inteligentBot():

    def __init__(self, _gameBeingPlayed, _character):
        self.botNetwork = neuroNetwork()
        self.game = _gameBeingPlayed
        self.character = _character
        self.neutralCharacter = self.game.neutralCharacter

    def Read(self):
        for a in range(1,10):
            if (self.game.board[a] == self.game.neutralCharacter):
                self.botNetwork.input[a] = int(0)
            elif (self.game.board[a] == self.character):
                self.botNetwork.input[a] = int(1)
            elif (self.game.board[a] == self.game.neutralCharacter):
                self.neuroNetwork.input[a] = int(-1)
            else:
                print("Nope")
            print (self.botNetwork.input[a])

    def TakeDecision(self):
        max = -1
        nextMove = 0
        for a in range (10):
            if self.botNetwork.synaptic_output[a] > max:
                nextMove = a 
                max = self.botNetwork.synaptic_output[a]

    def Move(self):
        self.Read()
        self.TakeDecision()
        return 0

    def readTable():
        return 0


if __name__ == "__main__":
    test = neuroNetwork()
    test.debug(1)
