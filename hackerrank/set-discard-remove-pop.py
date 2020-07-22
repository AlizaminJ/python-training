# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))
print(sum(s))

# n = int(input())
# s = set(map(int, input().split())) 
# t = int(input())

# for i in range(t):
#     c, *args = map(str,input().split())
#     getattr(s,c) (*(int(x) for x in args))
# print (sum(s))