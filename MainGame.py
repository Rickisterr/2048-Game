"""
Code developed from scratch by Richik Sinha

Steps for the game functioning (All functions are members of the GameBoard):
(0) CheckState and generate a square initially
(1) Running loop until state is 3 or 2 when loop ends
(2) Wait for user input and merge any adjacent equal squares in that direction
(3) Move all squares to the farthest point in the inputted direction
(4) CheckState
(5) Generate a square piece at random at an empty space
(6) CheckState and go to step 1
"""
import random                       # Random number generation purposes



##### Class to define the gameboard and the functions performable on the same
class GameBoard:
    
    #### Member variables that describe the state of the board
    def __init__(self):
        """
        The positions of the board are displayed as a nested list where the
        rows are signified by the elements in the outer list and the index of
        each element in the list signifying the rows indicates the corresponding
        column of the element.
        Thus, to access a particular element, BoardGrid[row-1][column-1] is used.
        """
        # Privatized to class
        self.__BoardGrid = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]                  # Describes the layout of the board (0 indicates empty square in grid)
        
        self.adjacentEqls = []      # contains info on the adjacent squares which are equal
        # Each element in adjacentEqls is depicted as [row, column, axis]
        # where (row, column) and (row, column+1) are equal if axis is 0
        # and (row, column) and (row+1, column) are equal if axis is 1
        
        self.state = 1              # describes state of the board: 1-playable, 2-deadend, 3-winner
        
        self.emptySquares = []      # describes the index number of all empty squares at a time on the board (0 is top left, 15 is bottom right)



    #### Member function to check for state of board
    def checkState(self):
        
        self.state = 2              # State is initialized to be deadend unless an empty space or 2048 present or playable squares left
        self.adjacentEqls = []      # adjacentEqls is reset for rechecking
        self.emptySquares = []      # resetting emptySquares to recheck
        
        for iterRow in range(1, 5):             # Iterating through Rows
            for iterCol in range(1, 5):         # Iterating through each row's elements
                
                if(self.__BoardGrid[iterRow-1][iterCol-1] == 2048):       # If 2048 piece is present, state is winner and function returns immediately
                    self.state = 3
                    return
                
                elif(self.__BoardGrid[iterRow-1][iterCol-1] == 0):        # If an empty space is detected, state is playable
                    self.state = 1
                    
                    # Updating emptySquares with index of empty square
                    self.emptySquares.append(int( ( 4 * (iterRow - 1) ) + ( iterCol - 1 ) ))
                
                else:                                                     # If not empty square or won
                    
                    ## Horizontally equal squares check
                    if(iterCol != 4):                                         # Checking that iterCol is not pointing to the index of the last column
                        # Next, check if two horizontally adjacent elements are equal; if so, playable
                        if(self.__BoardGrid[iterRow-1][iterCol-1] == self.__BoardGrid[iterRow-1][iterCol]):
                            self.state = 1
                            
                            self.adjacentEqls.append( [ iterRow, iterCol, 0 ] ) # Indicates (iterRow, iterCol) and (iterRow, iterCol+1) are equal
                    
                    ## Vertically equal squares check
                    if(iterRow != 4):                                         # Checking that iterRow is not pointing to the index of the last row
                        # Next, check if two vertically adjacent elements are equal; if so, playable
                        if(self.__BoardGrid[iterRow-1][iterCol-1] == self.__BoardGrid[iterRow][iterCol-1]):
                            self.state = 1
                            
                            self.adjacentEqls.append( [ iterRow, iterCol, 1 ] ) # Indicates (iterRow, iterCol) and (iterRow+1, iterCol) are equal
        
        """
        If no other condition is met, the state remains deadend,
        where the entire board is filled without playable squares
        and returned; otherwise met condition is communicated by state
        """
        return

    
    
    #### Member function used to randomly generate board squares in empty spaces
    def generateSquare(self):
        if(len(self.emptySquares) == 0):                    # If no empty squares, skip square generation
            return
        
        # GenMax is used to get a random number between 1 and the number of 
        # empty squares on board to iterate through them and pick a random
        # empty square to generate a new square inside of
        GenMax = random.randint( 0, len(self.emptySquares)-1 )
        
        # Generating a piece 2 at the square pointed to by the index in the GenMax-th element in emptySquares
        self.__BoardGrid[self.emptySquares[GenMax] // 4][self.emptySquares[GenMax] % 4] = 2
        
        return
    
    
    
    #### Member function used for debugging and tracking purposes (displays all variables)
    def displayCheck(self):
        
        ## Printing the board
        print("Board: ")
        for pr in range(4):
            print("     ", self.__BoardGrid[pr][0], " " * (6 - len(str(self.__BoardGrid[pr][0]))), end="")
            print(self.__BoardGrid[pr][1], " " * (6 - len(str(self.__BoardGrid[pr][1]))), end="")
            print(self.__BoardGrid[pr][2], " " * (6 - len(str(self.__BoardGrid[pr][2]))), end="")
            print(self.__BoardGrid[pr][3], " " * (6 - len(str(self.__BoardGrid[pr][3]))), end="\n\n")
        
        print("State: ", self.state)                        ## Printing the board state
        
        print("\n\nAdjacent Squares: ", self.adjacentEqls)  ## Printing the leftmost or topmost of the pair of all adjacent squares present ([ Row, Col, Axis ])
        
        print("\n\nEmpty Indices: ", self.emptySquares)     ## Printing list of indices of all empty squares on board

        return

##### END OF GameBoard CLASS



def debug():
    # Creating an object Board from GameBoard to affect the game board
    BoardDebug = GameBoard()
    
    BoardDebug.checkState()
    BoardDebug.displayCheck()



def main():
    # Initiating an instance of GameBoard to produce a Board to play on
    Board = GameBoard()
    
    # Initially checking state and generating the first square to begin playing
    Board.checkState()
    Board.generateSquare()
    
    # Moving to loop to keep the game running until state reaches deadend or winning state
    while(Board.state not in [2, 3]):
        print("Currently unending")
    
    # Win state (2048 reached)
    if(Board.state == 3):
        print("+-----------------------------------------------------------------------------------------+")
        print("|                                                                                         |")
        print("|      88     88    888888    88      88          88        88  888888  888      88       |")
        print("|       88   88    88    88   88      88          88   88   88    88    8888     88       |")
        print("|        88 88    88      88  88      88          88   88   88    88    88 88    88       |")
        print("|         888     88      88  88      88          88   88   88    88    88  88   88       |")
        print("|         888     88      88  88      88          88   88   88    88    88   88  88       |")
        print("|         888     88      88  88      88          88   88   88    88    88    88 88       |")
        print("|         888      88    88    88    88           88   88   88    88    88     8888       |")
        print("|         888       888888      888888             8888  8888   888888  88      888       |")
        print("|                                                                                         |")
        print("+-----------------------------------------------------------------------------------------+")
    
    # Lose state (Board filled with no possible moves left)
    elif(Board.state == 2):
        print("+---------------------------------------------------------------------------------------------------+")
        print("|                                                                                                   |")
        print("|      88     88    888888    88      88          88           888888      888888   888888888       |")
        print("|       88   88    88    88   88      88          88          88    88   888    88  88              |")
        print("|        88 88    88      88  88      88          88         88      88  88         88              |")
        print("|         888     88      88  88      88          88         88      88   88888     8888888         |")
        print("|         888     88      88  88      88          88         88      88      8888   88              |")
        print("|         888     88      88  88      88          88         88      88         88  88              |")
        print("|         888      88    88    88    88           88          88    88   88    888  88              |")
        print("|         888       888888      888888            888888888    888888     888888    888888888       |")
        print("|                                                                                                   |")
        print("+---------------------------------------------------------------------------------------------------+")



if(__name__ == "__main__"):
    debug()