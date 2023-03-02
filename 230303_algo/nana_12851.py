# 숨바꼭질2
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
sec, route = 21e8, 0

def bfs(N, K):
    global sec, route
    q = deque()
    visited = list()
    # 위치, 시간
    q.append([N, 0])
    visited.append([N, 0])
    while q:
        loc, time = q.popleft()
        if loc == K and sec >= time:
            sec = time
            route += 1
            # print(sec, route)
        elif time < sec:
            if [loc+1, time+1] not in visited:
                q.append([loc+1, time+1])
                visited.append(loc+1)
            if [loc-1, time+1] not in visited:
                q.append([loc-1, time+1])
                visited.append(loc-1)
            if [loc*2, time+1] not in visited:
                q.append([loc*2, time+1])
                visited.append(loc*2)

bfs(N, K)
print(sec)
print(route)
        