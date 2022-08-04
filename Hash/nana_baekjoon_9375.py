# 패션왕 신해빈
import sys
input = sys.stdin.readline
N = int(input())
wardrobe = dict()

for _ in range(N):
    sum = 1
    num = int(input())
    for _ in range(num):
        wear, kind_of_wear = input().split()
        # print(wear, kind_of_wear)
        if kind_of_wear in wardrobe:
            wardrobe[kind_of_wear].append(wear)
        else:
            wardrobe[kind_of_wear] = list()
            wardrobe[kind_of_wear].append(wear)
    # print(wardrobe)
    for i in wardrobe.values():
        j = len(i) + 1
        sum *= j
    wardrobe.clear()
    print(sum - 1)