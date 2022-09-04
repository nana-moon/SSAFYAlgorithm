# 영단어 암기는 어려워
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
word_list = dict()

for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue    
    elif word not in word_list:
        word_list[word] = 1
    else:
        word_list[word] += 1
# word_list.sort()

new_list = sorted(word_list.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))
# print(new_list)
for i in new_list:
    print(i[0])
