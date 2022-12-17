# 특정한 최단 경로
import sys
import heapq
input = sys.stdin.readline

def dijkstra(st, ed):
    result = [21e8]*N
    heap =[]
    
    # 비용, 경유지 순으로 push (적은 비용 순으로 pop하기 위해서)
    heapq.heappush(heap, [0, st])
    result[st] = 0 # 시작점
    while heap:
        cost, mid = heapq.heappop(heap) # 비용, 경유지
        if result[mid] < cost: continue # 큐에서 pop한 경유지 비용 vs result에 업데이트 되어있는 경유지 비용
        for i in arr[mid]: # 경유지에서 접근 가능한 모든 도착점 순회
            detour = cost + i[1] # 시작점 > 경유지 > 도착점 비용
            if detour < result[i[0]]: # 시작점 > 도착점 비용이랑 비교
                result[i[0]] = detour
                heapq.heappush(heap, (detour,i[0])) # 업데이트 될 경우 도착점을 새로운 경유지로 만듦
    return result[ed]

N, E = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a-1].append([b-1, c])
    arr[b-1].append([a-1, c])
    
A, B = map(int, input().split())
A -= 1
B -= 1
result_A = dijkstra(0,A) + dijkstra(A,B) + dijkstra(B, N-1)
result_B = dijkstra(0,B) + dijkstra(B,A) + dijkstra(A, N-1)

if result_A >= 21e8 or result_B >= 21e8:
    print(-1)
else:
    print(min(result_A, result_B))
