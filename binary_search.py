arr = [1,2,3,4,5,6,7,8]
to_be_searched = 5
left = 0
right = 0 

while arr[left] < arr[right]:
    mid = (left + right) // 2
    for i in range(0, len(arr)):
        if to_be_searched == arr[mid]:
            print(i)

        if to_be_searched < arr[mid]:
            right = mid - 1
        elif to_be_searched > arr[mid]:
            left = mid + 1


        