# 경쟁적 전염
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

q = deque()
virus = []

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            virus.append([arr[i][j], i, j])

virus.sort(key=lambda x:x[0])

for vir in virus:
    q.append([vir[1],vir[2],0])

dy = [0,0,1,-1]
dx = [1,-1,0,0]
while q:
    i, j, time = q.popleft()
    if time == S:
        break
    for k in range(4):
        ny = dy[k] + i
        nx = dx[k] + j
        if 0<=ny<N and 0<=nx<N and arr[ny][nx] == 0:
            arr[ny][nx] = arr[i][j]
            q.append([ny,nx, time+1])
print(arr[X-1][Y-1])