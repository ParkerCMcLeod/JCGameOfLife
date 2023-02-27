# JC's Game of Life in Python
# Parker McLeod and Brice Turner
  
# RULES:
# 
# Any live cell with two or three live neighbors survives to the next generation.
# Any dead cell with three live neighbors becomes a live cell in the next generation.
# All other live cells die in the next generation, and all other dead cells remain dead.

import time
import numpy as np
import matplotlib.pyplot as plt

RANDOM_START = True
INITIAL_DENSITY = 0.2 

BOARD_SIZE = 40 # num cells in row of square
STEP_TIME = .2 # (s)
MAX_STEPS = 20 # (s)


# Fills a RANDOM_START x RANDOM_START board up
def SetupBoard():
    # Create the board var
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=np.int8)

    # Fill initial vals (or not)
    if(RANDOM_START):
        board[np.random.random((BOARD_SIZE, BOARD_SIZE)) < INITIAL_DENSITY] = 1

    return board


# Iterates the simulation by one step 
def StepSimulation(board):
    # iterate over each cell in the board
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # Count the number of live neighbors for the current cell
            num_neighbors = np.sum(board[max(0, i-1):min(BOARD_SIZE, i+2), max(0, j-1):min(BOARD_SIZE, j+2)]) - board[i, j]
            
            # Apply the rules of the Game of Life to determine the new state of the cell
            if board[i, j] == 1 and (num_neighbors == 2 or num_neighbors == 3):
                board[i, j] = 1
            elif board[i, j] == 0 and num_neighbors == 3:
                board[i, j] = 1


def DisplaySimulation(board):
    plt.imshow(board, cmap='binary')
    plt.xticks([])
    plt.yticks([])
    plt.draw()
    plt.pause(0.001)

def JCGOLDriver():
    board = SetupBoard()

    numSteps = 0
    while(numSteps <= MAX_STEPS):
        StepSimulation(board)
        DisplaySimulation(board)
        time.sleep(STEP_TIME) # wait for a moment before displaying the next step in sim
        numSteps += 1

JCGOLDriver()
