"""
The inteligent BOT
"""

import random

class neuroNetwork(Object):
    def __init__(self):
        random.seed(5)
        # We model a single neuron, with 3 input connections and 1 output connection.
        # We assign random weights to a 3 x 1 matrix, with values in the range -1 to 1
        # and mean 0.
        self.synaptic_weights = 2 * random.random((3, 1)) - 1 

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

class inteligentBot(Object):

    def __init__(self):

    def neuron:
