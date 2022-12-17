# 입국심사
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
judges = [int(input()) for _ in range(N)]
max_time = min(judges) * M
exits = []
for judge in judges:
    for i in range(1, max_time):
        exits.append(judge*i)
exits.sort()
print(exits[M-1])