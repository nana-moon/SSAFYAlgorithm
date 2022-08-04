# 문자열 집합
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
dictionary = dict()
count = 0
for _ in range(N):
    word = input()
    if word not in dictionary:
        dictionary[word] = 1
    dictionary[word] += 1
for _ in range(M):
    search = input()
    if search in dictionary:
        count += 1
print(count)