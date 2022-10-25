# 포도주 시식
import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
max_lst = [0]*N

max_lst[0] = lst[0]

if N > 1: # 2
    max_lst[1] = lst[0] + lst[1]
if N > 2: # 3
    max_lst[2] = max(lst[0]+lst[1], lst[1]+lst[2], lst[0]+lst[2])
if N > 3: # 4
    for i in range(3, N):
        max_lst[i] = max(lst[i] + max_lst[i-2], lst[i]+lst[i-1] + max_lst[i-3], max_lst[i-1])
    
print(max_lst[N-1])