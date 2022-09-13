# 스타트링크
from collections import deque
import sys
input = sys.stdin.readline

top, now, target, up, down = map(int, input().split())

now -= 1
target -= 1

visited = [False]*10000000
que = deque()
que.append(now)
visited[now] = True

cnt = 0
flag = 0

while que:
    tmp = que.popleft()
    if tmp == target:
        break
    elif tmp < target:
        new = tmp + up
        if visited[new] == True:
            flag = 1
            break
        else:
            visited[new] = True
            cnt += 1
            que.append(new)
    else:
        new = tmp - down
        if visited[new] == True:
            flag = 1
            break
        else: 
            visited[new] = True
            cnt += 1
            que.append(new)
if flag:
    print('use the stairs')
else:
    print(cnt)  
         
