# JC's Game of Life in Python
# Parker McLeod and Brice Turner
  
import time
import numpy as np


BoardSize = 40 # sqrt of num cells in board
RANDOM_START = True
INITIAL_DENSITY = 0.2
STEP_TIME = .2 # in seconds


def SetupBoard():
    # Create the board
    board = [[0 for x in range(BoardSize)] for y in range(BoardSize)]

    # Initialize the board with nothing
    board = np.zeros((BoardSize, BoardSize), dtype=np.int8)

    # Fill initial values
    if(RANDOM_START):
        board[np.random.random((BoardSize, BoardSize)) < INITIAL_DENSITY] = 1


def step_simulation():

def display_simulation():

def JCGOLDriver():

    time.sleep(STEP_TIME) # wait for a moment before displaying the next step in sim