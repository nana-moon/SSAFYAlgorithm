# K번 작업에 대해 선행 관계에 있는 작업들의 번호는 모두 1 이상 (K-1) 이하이다.
# 위 조건 때문에 이렇게 dp로 풀어도 된다.

import sys
input = sys.stdin.readline
n = int(input())
times = [0] *(n+1)
graph = {}

for i in range(1, n+1):
    lst = list(map(int, input().split()))
    times[i] = lst[0]
    if lst[1] == 0:
        continue
    for j in lst[2:]:
        if i in graph:
            graph[i].append(j)
        else:
            graph[i] = [j]
# print(graph)

for i in range(1, n+1):
    if i in graph:
        time = 0
        for j in graph[i]:
            time = max(time, times[j])
        times[i] += time

print(max(times))
        
            
			
        
    
    