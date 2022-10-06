#Given an array of integers your solution should 
# find the smallest integer. 

def find_smallest_int(arr):
    min=arr[0]
    for i in arr:
        if i<min:
            min=i
    return min

array = [1,3,-4,5,6,7,8]
print(find_smallest_int(array))