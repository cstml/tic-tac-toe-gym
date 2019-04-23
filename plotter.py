"""
Class that helps with the graphical analysis of what the bot is doing
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
# Sets Python as a 
import matplotlib.pyplot as plt

class plotAnalaysis (object):

    def __init__ (self):
        self.fig, self.ax = plt.subplots()
        a = np.array([1,2,3])
        self.ax.plot (a)
        plt.show()

    def Show (self):
        self.ax.plt.show()

if __name__ == '__main__':
    d = plotAnalaysis()
    """Debug
    d.Show()
    fig, ax = plt.subplots()
    ax.plot (a)
    ax.plot (b)
    plt.show()
    """
