# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

n = int(input())
arr = list(map(int, input().split()))
largest = max(arr)

for _ in range(n):
    if largest == max(arr):
        arr.remove(max(arr))

print(max(arr))