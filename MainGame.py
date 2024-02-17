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
        
        self.state = 1              # describes state of the board: 1-playable, 2-deadend, 3-winner
        
        self.emptySquares = []      # describes the index number of all empty squares at a time on the board (0 is top left, 15 is bottom right)



    #### Member function to check for state of board
    def checkState(self):
        
        self.state = 2              # State is initialized to be deadend unless an empty space or 2048 present or playable squares left
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
                            continue
                            
                    ## Vertically equal squares check
                    if(iterRow != 4):                                         # Checking that iterRow is not pointing to the index of the last row
                        # Next, check if two vertically adjacent elements are equal; if so, playable
                        if(self.__BoardGrid[iterRow-1][iterCol-1] == self.__BoardGrid[iterRow][iterCol-1]):
                            self.state = 1
                            continue
        
        """
        If no other condition is met, the state remains deadend,
        where the entire board is filled without playable squares
        and returned; otherwise met condition is communicated by state
        """
        return
    
    
    
    #### Member function used to combine any adjacent equal elements
    def adjacentAdd(self, dir):                             # dir = 1, 2, 3, 4 for left, up, down, right
        if(dir in [1, 4]):
            
            # Checking for horizontally adjacent squares to combine and combining according to direction
            for iterRow in range(0, 4):
                for iterCol in range(0, 3):
                    i = iterCol + 1
                    
                    # Finding the next non empty piece
                    while((i < 4) and (self.__BoardGrid[iterRow][i] == 0)):
                        i += 1
                    
                    # If next non empty element is equal to current, double current and empty the other square
                    if((i < 4) and (self.__BoardGrid[iterRow][i] == self.__BoardGrid[iterRow][iterCol])):
                        if(dir == 1):
                            self.__BoardGrid[iterRow][iterCol] = 2 * self.__BoardGrid[iterRow][iterCol]
                            self.__BoardGrid[iterRow][i] = 0
                        else:
                            self.__BoardGrid[iterRow][i] = 2 * self.__BoardGrid[iterRow][i]
                            self.__BoardGrid[iterRow][iterCol] = 0
        
        elif(dir in [2, 3]):
            
            # Checking for vertically adjacent squares to combine and combining according to direction
            for iterRow in range(0, 3):
                for iterCol in range(0, 4):
                    i = iterRow + 1
                    
                    # Finding the next non empty piece
                    while((i < 4) and (self.__BoardGrid[i][iterCol] == 0)):
                        i += 1
                    
                    # If next non empty element is equal to current, double current and empty the other square
                    if((i < 4) and (self.__BoardGrid[i][iterCol] == self.__BoardGrid[iterRow][iterCol])):
                        if(dir == 1):
                            self.__BoardGrid[iterRow][iterCol] = 2 * self.__BoardGrid[iterRow][iterCol]
                            self.__BoardGrid[i][iterCol] = 0
                        else:
                            self.__BoardGrid[i][iterCol] = 2 * self.__BoardGrid[i][iterCol]
                            self.__BoardGrid[iterRow][iterCol] = 0
                    
                    

    
    
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
    
    
    
    #### Member function to perform moves on the board according to inputs
    def movePieces(self, dir):                  # dir = 1, 2, 3, 4 for left, up, down and right directional moves respectively
        
        # Combining all elements before moving
        self.adjacentAdd(dir)
        
        if(dir in [1, 4]):                      # If movement is along horizontal axis, change second piece to 0 and double the first
            
            # Moving all pieces right where possible
            if(dir == 4):
                for iterRow in range(0, 4):
                    
                    for iterCol in range(0, 3):
                        iterCol_rev = 2 - iterCol           # Iterating backwards through a row's column
                        temp = iterCol_rev + 1
                        
                        # Skip square if current square is empty
                        if(self.__BoardGrid[iterRow][iterCol_rev] == 0):
                            continue
                        
                        # Finding the next non empty square
                        while((temp < 4) and (self.__BoardGrid[iterRow][temp] == 0)):
                            temp += 1
                        
                        temp -= 1
                        
                        # Swapping empty space and current piece
                        if(temp >= iterCol_rev + 1):
                            self.__BoardGrid[iterRow][iterCol_rev], self.__BoardGrid[iterRow][temp] = self.__BoardGrid[iterRow][temp], self.__BoardGrid[iterRow][iterCol_rev]
            
            
            if(dir == 1):
                for iterRow in range(0, 4):
                    
                    for iterCol in range(1, 4):
                        temp = iterCol - 1
                        
                        # Skip square if current square is empty
                        if(self.__BoardGrid[iterRow][iterCol] == 0):
                            continue
                        
                        # Finding the next non empty square
                        while((temp >= 0) and (self.__BoardGrid[iterRow][temp] == 0)):
                            temp -= 1
                            
                        temp += 1
                        
                        # Swapping empty space and current piece
                        if(temp <= iterCol - 1):
                            self.__BoardGrid[iterRow][iterCol], self.__BoardGrid[iterRow][temp] = self.__BoardGrid[iterRow][temp], self.__BoardGrid[iterRow][iterCol]
            
            
            # Combining new adjacent equal elements
            for iterRow in range(0, 3):
                for iterCol in range(0, 2):
                    if(self.__BoardGrid[iterRow][iterCol] == self.__BoardGrid[iterRow][iterCol+1]):
                        self.__BoardGrid[iterRow][iterCol], self.__BoardGrid[iterRow][iterCol+1] = self.__BoardGrid[iterRow][iterCol+1], self.__BoardGrid[iterRow][iterCol]
                        
        
            
        
        # If movement is along vertical axis, change second piece to 0 and double the first
        if(dir in [2, 3]):

            # Moving all pieces where they need to be
            if(dir == 2):
                for iterRow in range(1, 4):
                    
                    for iterCol in range(0, 4):
                        temp = iterRow - 1
                        
                        # Skip square if current square is empty
                        if(self.__BoardGrid[iterRow][iterCol] == 0):
                            continue
                        
                        # Finding the next non empty square
                        while((temp >= 0) and (self.__BoardGrid[temp][iterCol] == 0)):
                            temp -= 1
                        
                        temp += 1
                        
                        # Swapping empty space and current piece
                        if(temp <= iterRow - 1):
                            self.__BoardGrid[iterRow][iterCol], self.__BoardGrid[temp][iterCol] = self.__BoardGrid[temp][iterCol], self.__BoardGrid[iterRow][iterCol]
            
            if(dir == 3):
                for iterRow in range(0, 3):
                    
                    for iterCol in range(0, 4):
                        iterRow_rev = 2 - iterRow           # Iterating backwards through a row's column
                        temp = iterRow_rev + 1
                        
                        # Skip square if current square is empty
                        if(self.__BoardGrid[iterRow_rev][iterCol] == 0):
                            continue
                        
                        # Finding the next non empty square
                        while((temp < 4) and (self.__BoardGrid[temp][iterCol] == 0)):
                            temp += 1
                        
                        temp -= 1
                        
                        # Swapping empty space and current piece
                        if(temp >= iterRow_rev + 1):
                            self.__BoardGrid[iterRow_rev][iterCol], self.__BoardGrid[temp][iterCol] = self.__BoardGrid[temp][iterCol], self.__BoardGrid[iterRow_rev][iterCol]
            
                   
    
    
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
    Board.generateSquare()
    Board.checkState()
    
    Board.displayCheck()
    
    # Moving to loop to keep the game running until state reaches deadend or winning state
    while(Board.state not in [2, 3]):
        print("\n")
        
        N = input("Enter a move: ").upper()
        
        match N:
            case "A":
                Board.movePieces(1)
            case "D":
                Board.movePieces(4)
            case "W":
                Board.movePieces(2)
            case "S":
                Board.movePieces(3)
            case _:
                continue
        
        Board.checkState()
        
        Board.generateSquare()
        
        Board.checkState()
        
        Board.displayCheck()
    
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
    main()