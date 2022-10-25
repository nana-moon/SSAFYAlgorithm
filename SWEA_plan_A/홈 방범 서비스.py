def count(i,j,k):
    cnt = 0
    for y in range(i-(k-1), i+(k-1)+1):
        if not (0<=y<N): continue
        length = (k-abs(i-y))*2-1
        tmp = length // 2
        for x in range(j-tmp, j+tmp+1):
            if not (0<=x<N): continue
            if arr[y][x] == '1':
                cnt += 1
    return cnt


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    Max_h = 0
    
    for k in range(1,N+2): ## 범위 중요
        cost = k*k +(k-1)**2
        # 최대 집의 개수
        for i in range(N):
            for j in range(N):
                cnt = count(i, j, k)
                if cnt*M - cost >= 0:
                    Max_h = max(Max_h, cnt)
                    
    print(f'#{tc} {Max_h}')
                