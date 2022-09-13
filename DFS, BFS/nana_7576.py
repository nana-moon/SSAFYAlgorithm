# 토마토
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
que = deque()

dy = [0,0,1,-1]
dx = [1,-1,0,0]

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            que.append([i, j])

while que:
    y, x = que.popleft()
    for k in range(4):
        ny = dy[k] + y
        nx = dx[k] + x
        if 0 <= ny < M and 0 <= nx < N and arr[ny][nx] == 0:
            arr[ny][nx] = arr[y][x] + 1
            que.append([ny, nx])

answer = 0
for ar in arr:
    for a in ar:
        if a == 0:
            print(-1)
            exit()
        elif answer < a:
            answer = a
            
print(answer - 1)