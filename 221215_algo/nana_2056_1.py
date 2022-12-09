# 작업 > 위상 정렬
from collections import deque
import copy

N = int(input())
# 작업 비용, 사전 작업의 수 나타낸 배열
cost, acc = [0 for _ in range(N+1)], [0 for _ in range(N+1)]

# 연결 관계를 나타낸 인접리스트
lst = [[] for _ in range(N+1)]


for i in range(N):
    tmp = list(map(int, input().split()))
    cost[i+1], acc[i+1] = tmp[0], tmp[1]
    if len(tmp) > 2:
        for t in tmp[2:]:
            #i+1의 사전작업이 t인 것임, t 다음에 할 수 있는 것이 i+1
            lst[t].append(i+1)
            
# idx 노드로 도착할 때 드는 누적 비용의 최대를 갱신할 배열
Max = copy.deepcopy(cost)

q = deque()
for i in range(1, N+1): # 사전 작업 수가 0이어서 바로 작업 가능한 것들을 q에 넣어줌
    if acc[i] == 0:
        q.append(i)
        
while q:
    now = q.popleft()
    n_cost = cost[now]
    for next in lst[now]:
        acc[next] -= 1
        Max[next] = max(cost[next]+Max[now], Max[next])
        if acc[next] == 0:
            q.append(next)

print(max(Max))

        
            
			
        
    
    