# https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import numpy as np

a=np.array(input().split(), int)
b=np.array(input().split(), int)

print(np.inner(a,b), np.outer(a,b), sep="\n")

# A,B = [np.array([input().split()],int) for _ in range(2)]
# print(np.inner(A,B))
# print(" ")
# print(np.inner(A,B)[0][0],np.outer(A,B),sep="\n")