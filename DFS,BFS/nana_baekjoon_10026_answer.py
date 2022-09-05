# 적록색약
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    que.append([x, y])
    used[x][y] = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == arr[x][y] and used[nx][ny] == 0:
                    que.append([nx, ny])
                    used[nx][ny] = 1

n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
used = [[0]*n for _ in range(n)]
que = deque()

cnt = 0
for i in range(n):
    for j in range(n):
        if used[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'
used = [[0]*n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if used[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)