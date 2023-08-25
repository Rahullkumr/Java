'''
valu: 1 2 3 4 5 6 7 8
indx: 0 1 2 3 4 5 6 7
'''

arr = [1,2,3,4,5,6,7,8]
to_be_searched = 5
left = 0
right = len(arr) - 1 #7


while arr[left] <= arr[right]:
    mid = (left + right) // 2 # 5
    if to_be_searched == arr[mid]:
        print(mid+1)
        break

    if to_be_searched < arr[mid]:
        right = mid - 1

    elif to_be_searched > arr[mid]:
        left = mid + 1
