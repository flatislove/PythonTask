#Given a non-empty array of integers, return the result of 
# multiplying the values together in order. 

def grow(arr):
    multi=1
    for i in arr:
        multi*=i
    return multi

print(grow([1,2,3,4,5]))