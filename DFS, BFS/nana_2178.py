# 미로 탐색
import sys
from collections import deque

input = sys.stdin.readline

def bfs(y, x):
    que = deque()
    que.append([y,x])
    while que:
        i, j = que.popleft()
        for k in range(4):
            ny = dy[k] + i
            nx = dx[k] + j
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if arr[ny][nx] == 0:
                continue
            if arr[ny][nx] == 1:
                arr[ny][nx] = arr[i][j] + 1
                que.append([ny,nx])
    return arr[N-1][M-1]

N, M = map(int, input().split())
arr = [list(map(int,input().strip())) for _ in range(N)]

dy = [0,0,1,-1]
dx = [1,-1,0,0]

print(bfs(0,0))




            
            