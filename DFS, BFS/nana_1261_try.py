# 알고스팟
import sys
from collections import deque

input = sys.stdin.readline

def dfs(y, x, cnt):
    # print(y,x)
    global answer
    if y == M-1 and x == N-1:
        print(y,x)
        if cnt < answer:
            answer = cnt
        return
    
    for k in range(4): 
        ny = dy[k] + y
        nx = dx[k] + x
        if ny < 0 or ny >= M or nx < 0 or nx >=N:
            continue
        if visited[ny][nx] == True:
            continue
        if arr[ny][nx] == 0:
            visited[ny][nx] = True
            dfs(ny,nx,cnt)
            visited[ny][nx] = False
        else:
            visited[ny][nx] = True
            dfs(ny,nx,cnt+1)
            # visited[ny][nx] = False
    
    


N, M = map(int, input().split()) # x, y
arr = [list(map(int,input().strip())) for _ in range(M)]

dy = [0,0,1,-1]
dx = [1,-1,0,0]
answer = 21e8
visited = [[False]*N for _ in range(M)]
visited[0][0] = True
dfs(0,0,0)
print(answer)