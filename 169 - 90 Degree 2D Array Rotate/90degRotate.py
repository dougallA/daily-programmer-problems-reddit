"""
Description:

Given a NxN size 2D array of numbers. Develop a way to rotate the data as if you rotated the data by 90 degrees clockwise.
Example:

N = 3

Data:

1 2 3
4 5 6
7 8 9

Rotate 90 degrees:

7 4 1
8 5 2
9 6 3

Rotate it again 90 degrees:

9 8 7
6 5 4
3 2 1

Challenge Input:

N = 10

1 2 3 4 5 6 7 8 9 0
0 9 8 7 6 5 4 3 2 1
1 3 5 7 9 2 4 6 8 0
0 8 6 4 2 9 7 5 3 1
0 1 2 3 4 5 4 3 2 1
9 8 7 6 5 6 7 8 9 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
9 8 7 6 7 8 9 8 7 6
0 0 0 0 0 0 0 0 0 0

Optional:

Show the 2D array at 90, 180, 270 degree clockwise from the original position.
"""

# Assuming that array read in from text file. 

def print_matrix(A):
    """
    :param A: 2D array
    """
    for i in range (len(A)):
        print A[i]

def rotate_by_90_cw(A):
    """
    :param A: 2D array
    """
    N = len(A)
    rotated_array = [[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            rotated_array[i][j] = test_array[N-j-1][i]
    return rotated_array


with open("data.txt", 'r') as data:
    test_array = ([[char for char in row if char != '\n' and char != ' '] 
                  for row in data.readlines()])

for r in range(0, 
               int(raw_input("Enter the number of 90deg CW rotations: "))):
    test_array = rotate_by_90_cw(test_array)
                            
print_matrix(test_array)
 

                      
                       

