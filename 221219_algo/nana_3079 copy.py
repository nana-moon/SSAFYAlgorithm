# 입국심사
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
judges = [int(input()) for _ in range(N)]
time = 0
cnt = 0
while cnt < M:
    time += 1
    for judge in judges:
        if judge <= time:
            if time % judge == 0:
                cnt += 1
print(time)
            