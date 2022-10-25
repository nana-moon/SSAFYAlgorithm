# 스타트와 링크
import sys
input = sys.stdin.readline

N = int(input()) # idx 0 ~ N-1
map = [list(map(int, input().split())) for _ in range(N)]

def powerSum(lst):
    sum = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            idx_y = lst[i]
            idx_x = lst[j]
            sum += map[idx_y][idx_x]
            sum += map[idx_x][idx_y]
    return sum

# N//2 명을 뽑는 알고리즘
picked = [0]*(N//2)
passed = [] # 중복 방지용
Min = 21e8

def pick(level, start):
    global Min
    if level == N//2:
        # print(picked)
        if picked not in passed:
            # 담아주기
            reverse = []
            for j in range(N):
                if j not in picked:
                    reverse.append(j)
            passed.append(reverse)
            
            # picked에 있는 것들을 더한 담에 최솟값이면 change
            result = abs(powerSum(reverse) - powerSum(picked))
            if result < Min:
                Min = result
        return
                        
    for i in range(start, N):
        picked[level] = i 
        pick(level+1, i+1)

pick(0,0)
print(Min)