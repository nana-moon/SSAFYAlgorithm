# 트리의 부모 찾기
# 루트부터 타고 내려가면서 부모랑 자식을 저장

N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]


for _ in range(N-1):
    i,j = map(int,input().split())
    arr[i][j] = 1
    arr[j][i] = 1
    
visited = [False]*(N+1)   
stack = [1] # root
result = [0]*(N+1)

while stack:
    root = stack.pop()
    visited[root] = True
    for i in range(len(arr[root])):
        if visited[i] == False and arr[root][i] == 1:
            visited[i] = True
            result[i]=root # i = 자식, root = 부모
            stack.append(i)
            
print(*result[2:], sep='\n')