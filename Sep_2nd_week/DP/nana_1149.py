# RGB거리
import sys
input = sys.stdin.readline
N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)] # 재귀 과정을 저장

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp [i-1][2]) + dp[i][0] # 마지막 선택 값이 빨강일 때 최소 비용
    dp[i][1] = min(dp[i-1][0], dp [i-1][2]) + dp[i][1] # 마지막 선택 값이 초록일 때 최소 비용
    dp[i][2] = min(dp[i-1][0], dp [i-1][1]) + dp[i][2] # 마지막 선택 값이 파랑일 때 최소 비용

print(min(dp[N-1])) 
    