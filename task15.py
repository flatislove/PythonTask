#In this Kata, you will be given a string and two indexes 
# (a and b). Your task is to reverse the portion of that 
# string between those two indices inclusive. 

def solve(s,a,b):
    return s[:a]+s[a:b+1][::-1]+s[b+1:]

print(solve('abcefghijklmnopqrstuvwxyz',0,20))