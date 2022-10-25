# 좋은수열
import sys
input = sys.stdin.readline

N = int(input())
result = []

def check(leng):
    L = (leng)//2 # 부분 수열 최대 길이
    for le in range(1, L+1):
        # if result[idx-leng+1:idx+1] == result[idx-2*leng+1: idx-leng+1]: return True
        if result[-le:] == result[-2*le:-le]: return True
    return False

def backTracking(leng):
    if check(leng):
        return -1
    if leng == N:
        print(*result, sep='')
        exit()
    for i in range(1,4):
        result.append(i)
        backTracking(leng+1)
        result.pop()

backTracking(0)
    
        
    
