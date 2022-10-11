def dfs(start, level):
    global Min
    if level == N//2:
        a_team = []
        b_team = []
        total_a = 0
        total_b = 0
        for i in range(N):
            if used[i]:
                a_team.append(i)
            else:
                b_team.append(i)
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                total_a += arr[a_team[i]][a_team[j]] + arr[a_team[j]][a_team[i]]
                total_b += arr[b_team[i]][b_team[j]] + arr[b_team[j]][b_team[i]]
        Min = min(abs(total_a-total_b), Min)
        return
    for i in range(start, N):
        used[i] = True
        dfs(i+1, level+1)
        used[i] = False
    

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [False]*N
    Min = 21e8
    dfs(0,0)
    print(f'#{tc} {Min}')