# Assuming that array read in from text file data.txt 

def print_matrix(A):
    for i in range (len(A)):
        print A[i]

def rotate_by_90_cw(A):
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
