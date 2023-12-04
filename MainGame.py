
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



    #### Member function to check for state of board
    def checkState(self):
        
        self.state = 2              # State is initialized to be deadend unless an empty space or 2048 present or playable squares left
        self.adjacentEqls = []      # adjacentEqls is reset for rechecking
        
        for iterRow in range(1, 5):             # Iterating through Rows
            for iterCol in range(1, 5):         # Iterating through each row's elements
                
                if(self.__BoardGrid[iterRow-1][iterCol-1] == 2048):       # If 2048 piece is present, state is winner and function returns immediately
                    self.state = 3
                    return
                
                elif(self.__BoardGrid[iterRow-1][iterCol-1] == 0):        # If an empty space is detected, state is playable
                    self.state = 1
                
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

    
    
    #### Member function used for debugging and tracking purposes (displays all variables)
    def displayCheck(self):
        
        ## Printing the board
        print("Board: ")
        for pr in range(4):
            print("     ", self.__BoardGrid[pr][0], end=" ")
            print(self.__BoardGrid[pr][1], end=" ")
            print(self.__BoardGrid[pr][2], end=" ")
            print(self.__BoardGrid[pr][3], end="\n\n")
        
        print("State: ", self.state)                        ## Printing the board state
        
        print("\n\nAdjacent Squares: ", self.adjacentEqls)  ## Printing the leftmost or topmost of the pair of all adjacent squares present ([ Row, Col, Axis ])

        return

##### END OF GameBoard CLASS



def main():
    Board = GameBoard()
    
    Board.checkState()
    Board.displayCheck()



if(__name__ == "__main__"):
    main()