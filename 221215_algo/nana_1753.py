# 최단경로 > 다익스트라
import sys
import heapq

def dijkstra(st):
    heap = []
    result[start] = 0 
    heapq.heappush(heap, [0, start]) # 비용 경유지로 둘 곳
    while heap:
        cost, mid = heapq.heappop(heap)
        
        if cost > result[mid]: continue
        
        # 경유지에서 갈 수 있는 곳 모두 방문
        for end in arr[mid]:

            n_cost = cost + end[1]
            if result[end[0]] > n_cost:
                result[end[0]] = n_cost
                heapq.heappush(heap, [n_cost, end[0]])


input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
start -= 1

arr = [[] for _ in range(V)]
INF = 21e8
result = [INF]*V

for _ in range(E):
    u, v, w = map(int, input().split()) # 시작점, 도착점, 비용
    u -= 1
    v -= 1 
    
    arr[u].append([v,w])
dijkstra(start)

for r in result:
    if r != INF:
        print(r, end=' ')
    else:
        print('INF')