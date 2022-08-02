import sys
from collections import deque
input = sys.stdin.readline
tc = int(input())
#테스트 케이스 입력 받기


for _ in range(tc):
    n, m = map(int, input().split())
    item_list = list(map(int, input().split()))
    idx_list = list(range(int(n)))
    cnt = 0
    
    while True:
        if m not in idx_list:
            print(cnt)
            break
        elif item_list[0] == max(item_list):
             item_list.pop(0)
             idx_list.pop(0)
             cnt += 1
             
        else:
            item_list.append(item_list.pop(0))
            idx_list.append(idx_list.pop(0))
            #뒤로 옮길때는 cnt 안올려도 됨




