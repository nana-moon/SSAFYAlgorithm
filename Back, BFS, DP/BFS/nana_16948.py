# 데스 나이트
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*N for _ in range(N)]
p1, p2, p3, p4 = map(int, input().split())
arr[p1][p2] = 1
arr[p3][p4] = 1

Min = 9999
def bfs(y,x):
    global Min
    used = [[False]*N for _ in range(N)]
    que = deque()
    que.append([y,x,0]) # y, x, cnt
    used[y][x] = True
    dy = [-2,-2,0,0,2,2]
    dx = [-1,1,-2,2,-1,1]
    
    while que:
        k, m, cnt = que.popleft()
        if k == p3 and m == p4:
            if cnt < Min:
                Min = cnt
            break
        for i in range(6):
            ny = dy[i] + k
            nx = dx[i] + m
            if 0>ny or ny>=N or 0>nx or nx>=N or used[ny][nx] == True:
                continue
            used[ny][nx] = True
            que.append([ny,nx,cnt+1])
                
bfs(p1,p2)

if Min != 9999:
    print(Min)
else:
    print(-1)