# 제로
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
stack = deque()
for _ in range(N):
    i = int(input())
    if i == 0:
        stack.pop()
    else:
        stack.append(i)
# 데크도 sum 함수 사용 가능
print(sum(stack))