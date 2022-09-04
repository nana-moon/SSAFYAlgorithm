# 섬의 개수
import sys
sys.setrecursionlimit(10**6)

def dfs(y,x):
    for i in range(8):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0<=ny<m and 0<=nx<n and visited[ny][nx] == False and arr[ny][nx]:
            visited[ny][nx] = True
            dfs(ny,nx)


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(m)]
    dy = [0,0,1,-1,1,-1,1,-1]
    dx = [1,-1,0,0,1,-1,-1,1]
    cnt = 0
    visited = [[False]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                dfs(i,j)
                cnt += 1

    print(cnt)