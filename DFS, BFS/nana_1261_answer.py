# 알고스팟
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # x, y
arr = [list(map(int,input().strip())) for _ in range(M)]

dy = [0,0,1,-1]
dx = [1,-1,0,0]

visited = [[False]*N for _ in range(M)]

que = deque()
que.append([0,0])
visited[0][0] = True
while que:
    y, x = que.popleft()
    if y == M-1 and x == N-1:
        print(arr[y][x])
        break
    for k in range(4): 
        ny = dy[k] + y
        nx = dx[k] + x
        if 0<=ny<M and 0<=nx<N and visited[ny][nx] == False:
            visited[ny][nx] = True
            if arr[ny][nx] == 0:
                arr[ny][nx] = arr[y][x]
                que.appendleft([ny,nx])
            else:
                arr[ny][nx] = arr[y][x] + 1
                que.append([ny,nx])
    print(arr)