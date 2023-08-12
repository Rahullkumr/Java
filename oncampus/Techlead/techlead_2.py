# 2. Write a program to sort the elements of an array in descending order without using built-in functions.

arr = [6, 2, 9, 12, 3]

print("Before sorting : ", arr)
print("After sorting in descending order: ", end=" ")

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(arr)