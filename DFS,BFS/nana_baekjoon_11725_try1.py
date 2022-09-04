# 트리의 부모 찾기
# 부모 노드란 타고 들어갔을 때 루트 노드가 1인 것
import sys
sys.setrecursionlimit(10**9)

def dfs(m):
    global flag
    if m == 1:
        flag = 1
        return
    for a in range(len(arr[m])):
        if arr[m][a] == 1 and visited[a] == False:
            visited[a] = True
            dfs(a)
            visited[a] = False


N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]


for _ in range(N-1):
    i,j = map(int,input().split())
    arr[i][j] = 1
    arr[j][i] = 1

# print(arr)
result = []
visited = [False]*(N+1)
for k in range(2,N+1):
    visited[k] = True
    for m in range(len(arr[k])):
        if arr[k][m] == 1 and visited[m] == False:
            flag = 0
            visited[m] = True
            dfs(m)
            visited[m] = False
            if flag:
                result.append(m)
                break
    visited[k] = False
print(*result, sep = '\n')