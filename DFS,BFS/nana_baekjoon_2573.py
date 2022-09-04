# 빙산
from collections import deque
import sys
import copy
input = sys.stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def melt():
    global arr, check
    new_arr =[[0]*M for _ in range(N)]
    new_check = []
    while check:
        i, j = check.pop()
        tmp = 0
        for k in range(4):
            ny = dy[k] + i
            nx = dx[k] + j
            if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 0:
                tmp += 1
        if arr[i][j] - tmp <= 0:
            new_arr[i][j] = 0

        else:
            new_arr[i][j] = arr[i][j] - tmp
            new_check.append([i,j])
    check = copy.deepcopy(new_check)
    arr = copy.deepcopy(new_arr)

def bfs(y, x):
    que = deque()
    visited[y][x] = True
    que.append([y,x])
    while que:
        y, x = que.popleft()
        for k in range(4):
            ny = dy[k] + y
            nx = dx[k] + x
            if 0<=ny<N and 0<=nx<M and visited[ny][nx] == False and arr[ny][nx] != 0:
                visited[ny][nx] = True
                que.append([ny,nx])
                
check = []                
for i in range(1,N-1):
    for j in range(1,M-1):
        if arr[i][j] != 0:
            check.append([i,j])

cnt = 0
while True:
    cnt += 1
    melt()
    visited = [[False]*M for _ in range(N)]
    flag = 0
    for i in range(N-1):
        for j in range(M-1):
            if visited[i][j] == False and arr[i][j] != 0:
                flag += 1
                if flag >= 2:
                    print(cnt)
                    exit()
                bfs(i,j)