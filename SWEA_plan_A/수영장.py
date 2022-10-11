for tc in range(1, int(input())+1):
    day, mon1, mon3, year = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0]*12
    dp[0] = min(arr[0]*day, mon1)
    dp[1] = min(arr[1]*day + dp[0], mon1 + dp[0])
    dp[2] = min(arr[2]*day + dp[1], mon1 + dp[1], mon3)
    
    for i in range(3, 12):
        dp[i] = min(dp[i-1]+arr[i]*day, dp[i-1]+mon1, dp[i-3]+mon3)
    
    result = min(year, dp[-1])
    print(f'#{tc} {result}')
