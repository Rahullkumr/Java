# Interchange first and last elements of an array using fn

def interchange(arr):
    first = arr[0]
    last = arr[-1]

    arr[0], arr[-1] = last, first
    
    return arr

arr = []
print("Enter 5 nos: ")
for i in range(5):
    arr.append(int(input()))

print(f"before interchange: {arr}")
print(f"After interchange: {interchange(arr)}")
