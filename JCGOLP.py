# JC's Game of Life in Python
# Parker McLeod and Brice Turner
  
# RULES:
# 
# Any live cell with two or three live neighbors survives to the next generation.
# Any dead cell with three live neighbors becomes a live cell in the next generation.
# All other live cells die in the next generation, and all other dead cells remain dead.

import numpy as np
import matplotlib.pyplot as plt

RANDOM_START = True
INITIAL_DENSITY = 0.2 

BOARD_SIZE = 40 # num cells in row of square
STEP_TIME = .3 # (s)
NUM_STEPS = 30 # (s)


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
    """
    Update the board according to the rules of Conway's Game of Life.
    
    Parameters:
        board (list of lists): The current state of the board.
        
    Returns:
        new_board (list of lists): The updated state of the board.
    """
    # Copy the current board to a new board so we can update it without affecting the original.
    new_board = [row[:] for row in board]
    
    # Define the rules of the game:
    # 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # 2. Any live cell with two or three live neighbours lives on to the next generation.
    # 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    
    # Loop through each cell in the board.
    for row in range(len(board)):
        for col in range(len(board[0])):
            # Count the number of live neighbors.
            live_neighbors = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    if row + i < 0 or row + i >= len(board) or col + j < 0 or col + j >= len(board[0]):
                        continue
                    if board[row + i][col + j] == 1:
                        live_neighbors += 1
            
            # Apply the rules of the game.
            if board[row][col] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[row][col] = 0
            else:
                if live_neighbors == 3:
                    new_board[row][col] = 1
    
    return new_board


def DisplaySimulation(board):
    plt.imshow(board, cmap='binary')
    plt.xticks([])
    plt.yticks([])
    plt.draw()
    plt.pause(STEP_TIME)

def JCGOLDriver():
    board = SetupBoard()

    numSteps = 0
    while(numSteps <= NUM_STEPS):
        StepSimulation(board)
        DisplaySimulation(board)
        numSteps += 1

JCGOLDriver()
