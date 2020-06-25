#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (numpy.transpose(array))
print (array.flatten())