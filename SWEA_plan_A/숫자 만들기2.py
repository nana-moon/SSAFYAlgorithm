def dfs(level, total):
    global max_total, min_total
    if level == N-1:
        max_total = max(max_total, total)
        min_total = min(min_total, total)
        return
 
    for i in range(4):
        if symbol[i] == 0: continue
        backup = total
        symbol[i] -= 1
        if i == 0:
 
            dfs(level+1, total+arr[level+1])
 
 
        elif i == 1:
 
 
            dfs(level+1, total-arr[level+1])
 
        elif i == 2:
 
 
            dfs(level+1, total*arr[level+1])
 
        elif i == 3:
            if total < 0:
                total = (-1)*(abs(total)//arr[level+1])
            else:
                total = total//arr[level+1]
            dfs(level + 1, total)
        total = backup
        symbol[i] += 1
        
        
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    symbol = list(map(int, input().split()))
    arr = list(map(int, input().split()))
 
    max_total = -21e8
    min_total = 21e8
 
    dfs(0, arr[0])
    print(f'#%d %d' %(test_case,max_total-min_total))