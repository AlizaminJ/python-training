# https://www.hackerrank.com/challenges/py-set-union/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&isFullScreen=true

n=int(input())
A = set(map(int, input().split())) 
b=int(input())
B = set(map(int, input().split())) 
print(len(A.union(B)))
# print(len(A|B))
