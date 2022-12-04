from collections import deque
import copy
# 연구소
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

Max = 0

def bfs():
    q = deque()
    tmp = copy.deepcopy(arr)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                q.append([i, j])
                
    while q:
        y, x= q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0<=ny<N and 0<=nx< M): continue
            if tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                q.append([ny, nx])
    total = 0
    for y in range(N):
        for x in range(M):
            if tmp[y][x] == 0:
                total += 1
    return total
                

def dfs(level):
    global Max
    if level == 3:
        Max = max(bfs(), Max)
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(level+1)
                arr[i][j] = 0
dfs(0)
print(Max)