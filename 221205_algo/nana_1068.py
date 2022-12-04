from collections import deque  

N = int(input())
tree = [[0]*N for _ in range(N)]
kill = [False]*N
arr = list(map(int, input().split()))

for i in range(N):
    if arr[i] != -1:
        tree[arr[i]][i] = 1
# print(tree)
first = int(input())

q = deque()
q.append(first)
kill[first] = True

while q:
    node = q.popleft()
    for i in range(N):
        if tree[node][i] == 1:
            q.append(i)
            kill[i] = True

leaf = 0

for i in range(N):
    if kill[i] == False:
        flag = 1
        for j in range(N):
            if tree[i][j] == 1:
                if kill[j] == False:
                    flag = 0
                    break
                
        if flag:   
            leaf += 1
print(leaf)