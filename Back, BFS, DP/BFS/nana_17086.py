# 아기 상어 2
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Max = 0

def bfs(i,j):
    used = [[False]*M for _ in range(N)]
    que = deque([(i,j,0)])
    used[i][j] = True
    while que:
        y, x, cnt = que.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 > nx or M <= nx or 0 > ny or N <= ny or used[ny][nx] == True: continue
            if arr[ny][nx] == 0:
                que.append([ny,nx,cnt+1])
                used[ny][nx] = True
            else:
                return cnt+1

dy = [0,0,1,-1,1,1,-1,-1]
dx = [1,-1,0,0,-1,1,-1,1]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            tmp = bfs(i,j)
            if tmp > Max:
                Max = tmp

print(Max)