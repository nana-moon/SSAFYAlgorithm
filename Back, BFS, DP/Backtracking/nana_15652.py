# N과 M (4)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 중복 순열
path = [0]*M
def dfs(level):
    if level == M:
        print(*path)
        return
    for i in range(1,N+1):
        if level > 0:
            if path[level-1] > i: # 백 트래킹
                continue  
        path[level] = i
        dfs(level+1)
        
dfs(0)