'''
    [1,2,3,4,6,7,10]
    Find missing nos in range of 1 to 10


    [1,2,2,3,3,4,5,6,7,7,8,5]
    o/p like: 2 is repeated 2 times
    only display the repeated ones
'''
def find_missing(arr):
    for no in range(1, 11):
        if no not in arr:
            print(no)


def print_repeated(array):
    unique_array = []
    for element in array:
        if element not in unique_array:
            unique_array.append(element)
            
    for i in unique_array:
        count = array.count(i)
        if count > 1:
            print(f"{i} is repeated {count} times")


arr = [1,2,3,4,6,7,10]
print(arr)
find_missing(arr)
print("\n-----------------------------------------------\n")


array = [1,2,2,3,3,4,5,6,7,7,8,5]
print(array)
print_repeated(array)
