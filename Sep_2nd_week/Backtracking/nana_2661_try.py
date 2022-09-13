# 좋은수열
import sys
input = sys.stdin.readline

N = int(input())
result = [0]*N

def check(idx):
    L = (idx + 1)//2 # 부분 수열 최대 길이
    for leng in range(1, L+1):
        for k in range(idx,leng):
            if k == 0: continue
            if 0 in result[k:k+leng]: break # 중요
            if result[k:k+leng] == result[k-leng:k]:
                return True # 중복 수열이 존재
    return False

for idx in range(N):
    num = 1
    while True:
        result[idx] = num
        # 중복 수열이 존재한다면 -> num +1 , 존재하지 않는다면 break
        if idx == 0: break
        if check(idx):
            num += 1
        else:
            break

print(*result, sep='')