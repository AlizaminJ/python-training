# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

n,m = map(int, input().split())
arr = map(int, input().split())

A=set(map(int, input().split()))
B=set(map(int, input().split()))

# happiness=0
# for i in arr:
#     if i in A:
#         happiness+=1
#     if i in B:
#         happiness-=1
# print(happiness)

print(sum([(i in A) - (i in B) for i in arr]))