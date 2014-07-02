"""
Description:

In construction there comes a need to compute the length and area of a jobsite. The areas and lengths computed are used by estimators to price out the cost to build that jobsite. If for example a jobsite was a building with a parking lot and had concrete walkways and some nice pavers and landscaping it would be good to know the areas of all these and some lengths (for concrete curbs, landscape headerboard, etc)

So for today's challenge we are going to automate the tedious process of calculating the length and area of aerial plans or photos.
ASCII Photo:

To keep this within our scope we have converted the plans into an ASCII picture. We have scaled the plans so 1 character is a square with dimensions of 10 ft x 10 ft.

The photo is case sensitive. so a "O" and "o" are 2 different blocks of areas to compute.
Blocks Counts, Lengths and Areas:

Some shorthand to follow:

    SF = square feet
    LF = linear feet

If you have the following picture.

####
OOOO
####
mmmm

    # has a block count of 2. we have 2 areas not joined made up of #
    O and m have a block count of 1. they only have 1 areas each made up of their ASCII character.
    O has 4 blocks. Each block is 100 SF and so you have 400 SF of O.
    O has a circumference length of that 1 block count of 100 LF.
    m also has 4 blocks so there is 400 SF of m and circumference length of 100 LF
    # has 2 block counts each of 4. So # has a total area of 800 SF and a total circumference length of 200 LF.

Pay close attention to how "#" was handled. It was seen as being 2 areas made up of # but the final length and area adds them together even thou they not together. It recognizes the two areas by having a block count of 2 (2 non-joined areas made up of "#" characters) while the others only have a block count of 1.
Input:

Your input is a 2-D ASCII picture. The ASCII characters used are any non-whitespace characters.
Example:

####
@@oo
o*@!
****

Output:

You give a Length and Area report of all the blocks.
Example: (using the example input)

Block Count, Length & Area Report
=================================

#: Total SF (400), Total Circumference LF (100) - Found 1 block
@: Total SF (300), Total Circumference LF (100) - Found 2 blocks
o: Total SF (300), Total Circumference LF (100) - Found 2 blocks
*: Total SF (500), Total Circumference LF (120) - Found 1 block
!: Total SF (100), Total Circumference LF (40) - Found 1 block

Easy Mode (optional):

Remove the need to compute the block count. Just focus on area and circumference length.
Challenge Input:

So we have a "B" building. It has a "D" driveway. "O" and "o" landscaping. "c" concrete walks. "p" pavers. "V" & "v" valley gutters. @ and T tree planting. Finally we have # as Asphalt Paving.

ooooooooooooooooooooooDDDDDooooooooooooooooooooooooooooo
ooooooooooooooooooooooDDDDDooooooooooooooooooooooooooooo
ooo##################o#####o#########################ooo
o@o##################o#####o#########################ooo
ooo##################o#####o#########################oTo
o@o##################################################ooo
ooo##################################################oTo
o@o############ccccccccccccccccccccccc###############ooo
pppppppppppppppcOOOOOOOOOOOOOOOOOOOOOc###############oTo
o@o############cOBBBBBBBBBBBBBBBBBBBOc###############ooo
ooo####V#######cOBBBBBBBBBBBBBBBBBBBOc###############oTo
o@o####V#######cOBBBBBBBBBBBBBBBBBBBOc###############ooo
ooo####V#######cOBBBBBBBBBBBBBBBBBBBOcpppppppppppppppppp
o@o####V#######cOBBBBBBBBBBBBBBBBBBBOc###############ooo
ooo####V#######cOBBBBBBBBBBBBBBBBBBBOc######v########oTo
o@o####V#######cOBBBBBBBBBBBBBBBBBBBOc######v########ooo
ooo####V#######cOOOOOOOOOOOOOOOOOOOOOc######v########oTo
o@o####V#######ccccccccccccccccccccccc######v########ooo
ooo####V#######ppppppppppppppppppppppp######v########oTo
o@o############ppppppppppppppppppppppp###############ooo
oooooooooooooooooooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooooooooooooooooooo

FAQ:

Diagonals do not connect. The small example shows this. The @ areas are 2 blocks and not 1 because of the Diagonal.
"""

class Grid:
    """
    Class representing the grid that the various rectangles lie in.
    In my implementation of this program the grids come in text files and 
    I make a 2d array to represent the contents of that text file.
    """
    def __init__(self, f):
        """
        Initializes the Grid. Grid is implemented as 2d array.

        :param f: The filename of the file that contains the ascii grid.
        """
        with open(f,'r') as gridfile:
            self.matrix = ([[char for char in row if char != '\n'] 
                            for row in gridfile.readlines()])
        # beginning represents the upper most 
        self.beginning = Square(0, 0, self)
    

    def walk(self):
        """
        Walks through the grid, computing the information using other 
        methods as it goes. Ultimately this will be the driver for 
        calculating the solution.
        """
        #print self.matrix
        current_spot = self.beginning
        while not (current_spot.row_num == len (self.matrix)-1 
                   and current_spot.col_num == len(self.matrix[0])-1):
            current_spot = current_spot.walk_right()


    def find_first_unexplored(self, bool_matrix):
        """
        Given a boolean matrix, finds the first 0 entry. Explores down columns 
        first, not rows!
        
        :returns: tuple of coordinates of the first 0 entry in bool_matrix
        Returns False is nothing found.
        """
        current_spot = self.beginning
        while not (current_spot.row_num == len (self.matrix)-1
                   and current_spot.col_num == len(self.matrix[0])-1):
            if bool_matrix[current_spot.row_num][current_spot.col_num] == 0:
                return (current_spot.row_num, current_spot.col_num) 
            current_spot = current_spot.walk_right()#####
        if (current_spot.row_num == len (self.matrix)-1
                   and current_spot.col_num == len(self.matrix[0])-1):
            if bool_matrix[current_spot.row_num][current_spot.col_num] == 0:
                return (current_spot.row_num, current_spot.col_num) 
        if current_spot.character == 0:
            return (self.row_num, self.col_num)
        return False

    def explore(self, char_dict = {}, bool_matrix = None):
        """
        Walks through the grid and calculates stuff 
        IMPROVE ABOVE LATER
        
        :param char_dict: A dictionary with the characters being found
        in the grid being the keys and the values being a tuple of 
        integers (B,C,A) where B is the number of blocks consisting
        of the key character, C is the circumference of the blocks
        made of the key character and A is the area of the blocks made 
        of the key character.

        :param bool_matrix: Matrix, initially filled with 0's of the
        same dimensions as the grid, wherein each entry represents the
        status of the exploration of that square. If that square has 
        been accounted for, the entry is a 0, otherwise it's a 1. 
        """
        if not bool_matrix:
            bool_matrix = [[0 for entry in row] for row in self.matrix]
        if self.find_first_unexplored(bool_matrix): 

            starting_coords = (self.find_first_unexplored(bool_matrix)[0], 
                               self.find_first_unexplored(bool_matrix)[1])

            unexplored_start = self.matrix[starting_coords[0]][starting_coords[1]]

            if not unexplored_start in char_dict:
                char_dict[unexplored_start] = (0,0,0)
            # else:
            #     char_dict[unexplored_start][0] += 1
                
            to_add = self.walk_row(starting_coords[0],
                                   starting_coords[1], bool_matrix)

            char_dict[unexplored_start]= (char_dict[unexplored_start][0]
                                          + to_add[2],
                                          char_dict[unexplored_start][1] 
                                          + to_add[0], 
                                          char_dict[unexplored_start][2] 
                                          + to_add[1])
            self.explore(char_dict, bool_matrix)
        return char_dict



    def walk_row(self, n, m, bool_matrix): #n,m coords
        """
        Starting at an unxplored square at position n,m, this function
        explores continuously to the right, so long as the character remains
        the same.

        :returns: tuple (b,c,a) representing how much row contributes to 
        block count, circumference, and area.
        """
        #import pdb; pdb.set_trace()
        current = Square(n, m, self)
        c,a,b = 0,0,0 #there is nothing to the left of the first 

        if not current.continues_to_right():
            if not current.continues_above():
                b = 1
                c += 10
            if not current.continues_below():
                c += 10
            if not current.continues_to_left():
                c += 10
            bool_matrix[current.row_num][current.col_num] = 1
            c += 10 #last square right.
            a += 100 #last square area
            return (c,a,b)

        while current.continues_to_right():
            bool_matrix[current.row_num][current.col_num] = 1
            a += 100
            if not current.continues_to_left():
                c += 10
            #nothing above it so top side adds to c
            if not current.continues_above():
                c += 10
            #nothing below it so top side adds to c
            if not current.continues_below():
                c += 10
            current = current.walk_right()

        return (c,a,b)
        
class Square:
    """
    This class represents a square on the grid. 
    """
    def __init__(self, row_num, col_num, master_grid):
        """
        Initializes the square. 

        :param row_num: The row of the grid that the Rectangle lies in.
        :param col_num: The column of the grid that the Rectangle lies in.
        :param master_grid: The Grid that this square belongs to.
        """
        self.character = master_grid.matrix[row_num][col_num]
        self.row_num = row_num
        self.col_num = col_num
        self.master_grid = master_grid


    def walk_right(self):
        """
        Advances to the next square in master grid.
        For now making it so that if it hits a newline it
        moves to the start of the next row. 
        :returns: the next Square object. 
        """
        if self.col_num == len(self.master_grid.matrix[0])-1 and self.row_num == len(self.master_grid.matrix)-1:
            return None
        if self.col_num == len(self.master_grid.matrix[0])-1:
            return Square(self.row_num+1, 0, self.master_grid)
        else:
            return Square(self.row_num, self.col_num + 1, self.master_grid)

    def walk_down(self):
        """
        Advances to the next square below in master grid.

        :returns: the next Square object. 
        """
        if self.col_num == len(self.master_grid.matrix[0])-1 and self.row_num == len(self.master_grid.matrix)-1:
            return None
        if self.row_num == len(self.master_grid.matrix)-1:
            return Square(0, self.col_num+1, self.master_grid)
        else:
            return Square(self.row_num + 1, self.col_num, self.master_grid)

        

    def continues_above(self):
        """
        Determines whether or not the character above this 
        square has the same character as the current square. 
        """
        if self.row_num == 0:
            return False
        return (self.master_grid.matrix[self.row_num-1][self.col_num] 
                == self.character)

    def continues_below(self):
        """
        Determines whether or not the charactr below this 
        square has the same character as the current square. 
        """
        if self.row_num == len(self.master_grid.matrix)-1:
            return False
        return (self.master_grid.matrix[self.row_num+1][self.col_num] 
                == self.character)

    def continues_to_left(self):
        """
        Determines whether or not the charactr to the left of this 
        square has the same character as the current square. 
        """
        if self.col_num == 0:
            return False
        return (self.master_grid.matrix[self.row_num][self.col_num-1] 
                == self.character )

    def continues_to_right(self):
        """
        Determines whether or not the charactr to the right of this 
        square has the same character as the current square. 
        """
        if self.col_num == len(self.master_grid.matrix[0])-1:
            return False
        return (self.master_grid.matrix[self.row_num][self.col_num+1] 
                == self.character)

def print_report(char_dict):
    print "Block Count, Length & Area Report"
    print "================================="
    print 
    for key in char_dict.keys():
        print (key + ": " + "Total SF (" + str(char_dict[key][2])
               + "), Total Circumference LF (" + str(char_dict[key][1]) 
               + ") - Found " + str(char_dict[key][0]) + " blocks"  )


if __name__ == '__main__':
    #test_grid = Grid('reddit-med-ex.txt')
    test_grid = Grid('toy-ex.txt')
    #test_grid.walk()
    #print_report(test_grid.explore())
    #print test_grid.walk_row(4,2)
    print test_grid.walkdown(test_grid.beginning)
