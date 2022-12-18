# 이모티콘 > DP
S = int(input())
dp = [21e8]*1002

dp[2], dp[3] = 2, 3
for i in range(4, 1002):
    for j in range(2, i//2 + 1):
        if i % j == 0:
            dp[i] = min(dp[i], dp[j] + i//j)
    # if i % 2 != 0:
    #     Min = min(Min, dp[(i+1)//2] + 3)
    for k in range(2, i): # 2 ~ i-1
        if dp[k] > dp[i] + i-k:
            dp[k] = dp[i] + i-k
    # if dp[i-1] > dp[i] + 1:
    #     dp[i-1] = dp[i]+1
print(dp[S])
        
    
    
                
                
        