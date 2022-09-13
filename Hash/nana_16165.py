# 걸그룹 마스터 준석이
import sys
import operator
# from tokenize import group

input = sys.stdin.readline
N, M = map(int, input().split())
girl_group = dict()
for _ in range(N):
    group_name = input().strip()
    # print(group_name)
    girl_group[group_name] = []
    num_member= int(input())
    for _ in range(num_member):
        member = input().strip()
        girl_group[group_name].append(member)
# print(girl_group)
for _ in range(M):
    question = input().strip()
    kind_of_quest = int(input())
    if kind_of_quest == 1:
        for group in girl_group:
            if question in girl_group.get(group):
                print(group)
    else:
        sorted_group = sorted(girl_group[question])
        print(*sorted_group, sep='\n')