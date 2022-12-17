# 카드 정렬하기 > heapq
import sys
import heapq

input = sys.stdin.readline
N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]

heapq.heapify(arr)
sum = 0
while (len(arr) > 1):
    min_sum = heapq.heappop(arr) + heapq.heappop(arr)
    sum += min_sum
    heapq.heappush(arr, min_sum)

print(sum)
    
    