# 트리의 부모 찾기
# 루트부터 타고 내려가면서 부모랑 자식을 저장
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
ad_list = [[] for _ in range(N + 1)]

for _ in range(N-1):
    i,j = map(int,input().split())
    ad_list[i].append(j)
    ad_list[j].append(i)
    
visited = [False]*(N+1)   
que = deque()
que.append(1)
result = [0]*(N+1)

while que:
    root = que.popleft()
    visited[root] = True
    for i in ad_list[root]:
        if visited[i] == False:
            visited[i] = True
            result[i]=root # 부모, 자식
            que.append(i)
            
print(*result[2:], sep='\n')