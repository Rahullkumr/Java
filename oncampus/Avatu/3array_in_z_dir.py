'''
array index:
    00 01 02
    10 11 12
    20 21 22

Question 1:
given array:
    1 2 3
    4 5 6
    7 8 9

Expected output (z shape):
    1 2 3
      5 
    7 8 9 

'''
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(3):
    for j in range(3):
        if i == 1 and j in (0,2):
            print(' ', end=" ")
        else:
            print(arr[i][j], end=" ")
    print()