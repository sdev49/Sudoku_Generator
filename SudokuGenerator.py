# # # # Imports # # # #
from random import randint, shuffle



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Step 1: Create Blank Grid~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Colour:
   BLUE = '\033[34;104m'
   RED = '\033[31;101m'
   END = '\033[0m'

class Difficulty:
   EASY = 'Easy'
   MED = 'Medium'
   HARD = 'Hard'

class SudokuBoard:
    """A data type representing a Sudoku board.
      | and - represent the edges of squares in the board.
      . represent a blank space in the board.
    """
    def __init__(self, difficulty):
        """Construct objects of type Board, with the given width and height."""
        self.width = 9
        self.height = 9
        self.data = [['x']*9 for row in range(9)]
        self.difficulty = difficulty

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ' _____________________________ ' + '\n'          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                # These statements color the X's and O's appropriately
                if col % 3 == 0 and col != 0:
                  if self.data[row][col] == "x":
                      s += '| . '
                  else:
                      s += '| ' + Colour.BLUE + self.data[row][col] + Colour.END + ' '
                else:
                  if self.data[row][col] == "x":
                      s += ' . '
                  else:
                      s += ' ' + Colour.BLUE + self.data[row][col] + Colour.END + ' '
            if (row+1) % 3 == 0 and (row+1) != 9:
              s += '|' +  '\n' + '|---------+---------+---------|' + '\n'
            else:
              s += '|' +  '\n'
        s += ' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ '   + '\n' # bottom of the board
        return str(s)       # the board is complete, return it


# # # # Create Sudoku Problem # # # #
# Step 1: Remove Cells (Create Problem)
# Step 2: Check Num Solutions

