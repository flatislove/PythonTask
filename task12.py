#Complete the function that takes two numbers as input, num 
# and nth and return the nth digit of num (counting from right 
# to left). Note If num is negative, ignore its sign and treat 
# it as a positive value If nth is not positive, return -1 
# Keep in mind that 42 = 00042. This means that findDigit(42, 5)
#  would return 0

import math

def find_digit(num, nth):
    if int(len(str(int(math.fabs(num))))<int(nth)): return 0
    elif nth>0: return int(str(int(math.fabs(num)))[len(str(int(math.fabs(num))))-nth])
    else: return -1

print(find_digit(0,20))
