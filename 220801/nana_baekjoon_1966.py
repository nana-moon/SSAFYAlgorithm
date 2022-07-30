# 프린터 큐
from collections import deque
import sys
# sr = 
N = int(input())
for _ in range(N):
    ea, idx = map(int, sys.stdin.readline().split())
    
    # 큐를 생성하고, 인덱스와 함께 넣는다.
    li = list(map(int, sys.stdin.readline().split()))
    que = deque()
    for tu in enumerate(li):
        que.append(tu)
    #print(que)
    
    # 몇 번째로 출력되는지를 count에 담음 
    count = 0
    
    # que가 존재할 때 게속 반복, que는 for문 요소 반복이 안되더라고 
    while que:
        # 큐에서 최댓값 찾기
        maximum = max(que, key = lambda x:x[1])
        
        # 맨 앞의 값을 pop
        target = que.popleft()
        # print(target, maximum)
        
        # 만약 최댓값이면서 인덱스가 일치하면 그대로 count + 1 후 반환, 밥복문 끝
        if target[1] == maximum[1] and target[0] == idx:
            count += 1
            print(count)
            break
        # 최댓값만 같다면 count +1
        elif target[1] == maximum[1]:
            count += 1
        # 최댓값이 아니라면 뒤로 보내줌
        else:
            que.append(target)
