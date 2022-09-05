# 트리의 부모 찾기
# 부모 노드란 타고 들어갔을 때 루트 노드가 1인 것

N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]


for _ in range(N-1):
    i,j = map(int,input().split())
    arr[i][j] = 1
    arr[j][i] = 1
    
visited = [False]*(N+1)   
stack = [1]
result = [0]*(N+1)

while stack:
    root = stack.pop()
    visited[root] = True
    for i in range(len(arr[root])):
        if visited[i] == False and arr[root][i] == 1:
            visited[i] = True
            result[i]=root # 부모, 자식
            stack.append(i)
            
print(*result[2:], sep='\n')