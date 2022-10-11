def dfs(y):
    global cnt, used_x, used_cross1, used_cross2
    if y == N:
        cnt += 1
        # print(arr)
        return
    
    back1 = used_x[:]
    back2 = used_cross1[:]
    back3 = used_cross2[:]
    
    for x in range(N):
        if x in used_x: continue
        if x+y in used_cross1: continue
        if x-y in used_cross2: continue
        used_x.append(x)
        used_cross1.append(x+y)
        used_cross2.append(x-y)
        # arr[y][x] = 1
        dfs(y+1)
        # arr[y][x] = 0
        used_x = back1[:]
        used_cross1 = back2[:]
        used_cross2 = back3[:]
        
for tc in range(1, int(input())+1):
    N = int(input())
    # arr = [[0]*N for _ in range(N)]
    used_x = list()
    used_cross1 = list() # 우 상향 대각선 중복 제거 i+j
    used_cross2 = list() # 우 하향 대각선 중복 제거 i-j
    cnt = 0
    dfs(0)
    print(f'#{tc} {cnt}')