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
        # We model a single neuron, with 3 input connections and 1 output connection.
        # We assign random weights to a 3 x 1 matrix, with values in the range -1 to 1
        # and mean 0.
        self.synaptic_weights = 2 * random.random((3, 1)) - 1 
        print (self.synaptic_weights)

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
        print (self.__sigmoid(self.synaptic_weights))
        print ()
        print (self.__sigmoid_derivative(self.synaptic_weights))
        print ()
        print (self.__sigmoid(input))
        print ()
        print (self.__sigmoid_derivative(input))

class inteligentBot():

    def __init__(self):
        return 0

    def neuron():
        return 0

if __name__ == "__main__":
    test = neuroNetwork()
    test.debug()
