# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy as np
np.set_printoptions(legacy='1.13')
n,m =map(int, input().split())
a=np.array([input().split() for _ in range(n)], int)

print(np.mean(a, axis=1), np.var(a, axis=0), np.std(a, axis=None), sep="\n" )