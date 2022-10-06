#Given a set of numbers, return the additive inverse of each. 
# Each positive becomes negatives, and the negatives become 
# positives.

def invert(lst):
    for i in range(len(lst)):
        lst[i]=lst[i]*(-1)
    return lst

array=[1,4,5,6,7,-2]
print(invert(array))