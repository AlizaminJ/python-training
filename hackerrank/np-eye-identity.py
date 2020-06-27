#https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

# print(numpy.identity(3)) #3x3dentity matrix
# print(numpy.eye(8,7, k=1)) #8x7 dimensional matrix with first upper diagonal 1

numpy.set_printoptions(legacy='1.13')
a, b=map(int, input().split(' '))
print(numpy.eye(a, b, k=0))


