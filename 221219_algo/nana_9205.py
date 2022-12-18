# 맥주 마시면서 걸어가기
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
	N = int(input())

	home_x, home_y = map(int, input().split())
	store = [list(map(int, input().split())) for _ in range(N)]
	penta_x, penta_y = map(int, input().split())
	used = [False]*N
	q = deque()
	q.append([home_x, home_y, used])
	is_happy = False
	while q:
		x, y, visited = q.popleft()
		if abs(penta_x-x) + abs(penta_y-y) <= 1000:
			is_happy = True
			break
		for i in range(N):
			store_x, store_y = store[i]
			if abs(store_x-x) + abs(store_y-y) <= 1000:
				if visited[i] == False:
					visited[i] = True
					q.append([store_x, store_y, visited])
	if is_happy:
		print('happy')
	else:
		print('sad')
          
   