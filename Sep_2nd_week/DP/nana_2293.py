# 동전 1
import sys 
input = sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [0]*(k+1) # dp[k] = k원이 되는 경우의 수
dp[0] = 1

# 중복 제거
for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])