#Simple, given a string of words, return the length of the 
# shortest word(s). String will never be empty and you do 
# not need to account for different data types.

def find_short(s):
    array=str(s).split(' ')
    l=len(s)
    for i in array:
        if len(str(i))<l: l=len(str(i))
    return l

print(find_short("sdfsdf sdf df sdf sd fff sd f"))
