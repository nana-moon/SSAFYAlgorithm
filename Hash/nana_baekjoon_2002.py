# 추월
import sys

input = sys.stdin.readline
N = int(input())
original = dict()
after = list()

for i in range(N):
    real_car = input()
    original[real_car] = i

for j in range(N):
    after_car = input()
    after.append(original.get(after_car))
# print(after)

# index 비교
result = set()
for car, idx_1 in original.items():
    for idx_2 in range(idx_1 + 1, N):
        if after.index(idx_1) > after.index(idx_2):
            result.add(idx_2)

print(len(result))

# 딕셔너리가 아니라 튜플을 요소로 하는 리스트 형태로 받아야하는 거 같다.