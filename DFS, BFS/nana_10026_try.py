# 적록색약
import copy
import sys
from collections import deque

input = sys.stdin.readline

def check(y, x, lst):
    global cnt 
    que = deque()
    que.append([y,x])
    used[y][x] = True
    
    while que:
        y, x = que.popleft()
        color = lst[y][x]
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<N and used[ny][nx] == 0:
                if lst[ny][nx] == color:
                    used[ny][nx] = cnt
                    que.appendleft([ny,nx])
                else:
                    cnt += 1
                    used[ny][nx] = cnt
                    que.append([ny,nx])

N = int(input())
arr = [list(input()) for _ in range(N)]
n_arr = copy.deepcopy(arr)
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            n_arr[i][j] = 'R'
        
cnt = 1
dy = [0,0,1,-1]
dx = [1,-1,0,0]
used = [[0]*N for _ in range(N)]  
# used[0][0] = True
check(0,0,arr)
print(used)
print(cnt)

cnt = 1
used = [[False]*N for _ in range(N)]         
used[0][0] = True
check(0,0,n_arr)
print(cnt)