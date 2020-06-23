#https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a=numpy.array(arr[::-1], float)
    return a
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
