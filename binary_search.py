arr = [1,2,3,4,5,6,7,8]
to_be_searched = 5
left = 0
right = 0 

while arr[left] < arr[right]:
    mid = left + right
    for i in range(0, len(arr)):
        if arr[mid] == to_be_searched:
            print(i)

        if arr[mid] 