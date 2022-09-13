# 스타트와 링크
import sys
input = sys.stdin.readline

N = int(input()) # idx 0 ~ N-1
map = [list(map(int, input().split())) for _ in range(N)]

picked = [False]*N
Min = 21e8

def pick(level, start):
    global Min
    if level == N//2:
        sum1, sum2 = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if picked[i] and picked[j]:
                    sum1 += map[i][j] + map[j][i]
                elif not picked[i] and not picked[j]:
                    sum2 += map[i][j] + map[j][i]
        Min = min(Min, abs(sum1-sum2))
        return
                        
    for i in range(start, N):
        picked[i] = True
        pick(level+1, i+1)
        picked[i] = False

pick(0,0)
print(Min)