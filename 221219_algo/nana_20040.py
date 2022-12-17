# 사이클 게임
import sys

# sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

boss_lst = [-1]*N
# print(boss_lst)

def find_boss(a):
    global boss_lst
    tmp_boss = boss_lst[a]
    if tmp_boss == -1: return a
    real_boss = find_boss(tmp_boss)
    boss_lst[a] = real_boss
    # while -1 != boss_lst[a]:
    #     a = boss_lst[a]
    return real_boss

def union(x, y):
    global boss_lst
    x_boss, y_boss = find_boss(x), find_boss(y)
    if x_boss == y_boss: return False # 그룹화 실패
    
    # 그룹화 - 작거나 같은 값 기준으로 합치면 트리의 길이가 짧아짐
    if x_boss > y_boss:
        boss_lst[x_boss] = y_boss
    else:
        boss_lst[y_boss] = x_boss
 


answer = 0
for i in range(1, M+1):
    st, ed = arr[i-1]
    # print(st, ed)
    flag = union(st, ed)
    
    if flag == False: # 그룹화 실패
        answer = i
        break

print(answer)