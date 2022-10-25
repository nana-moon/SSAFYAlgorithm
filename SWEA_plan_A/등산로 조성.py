from collections import deque
import copy

def bfs(arr):
    bfs_max = 0
    # used = [[False]*N for _ in range(N)]
    dy, dx = [0,0,1,-1], [1,-1,0,0]
    for i in range(len(m_lst)):
        # 깎여서 꼭대기가 아닌 경우
        if arr[m_lst[i][0]][m_lst[i][1]] != Max: continue
        q = deque()
        q.append((m_lst[i][0], m_lst[i][1], 1))
        while q:
            y,x,level = q.popleft()
            for j in range(4):
                ny = dy[j] + y
                nx = dx[j] + x
                if not(0<=ny<N and 0<=nx<N): continue
                if arr[ny][nx] >= arr[y][x]: continue
                q.append((ny,nx,level+1))
        bfs_max = max(bfs_max, level)
    return bfs_max


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 꼭대기 좌표, 꼭대기 값 구하기
    m_lst = []
    Max = 0
    for a in range(N):
        for b in range(N):
            if arr[a][b] > Max:
                Max = arr[a][b]
    for a in range(N):
        for b in range(N):
            if arr[a][b] == Max:
                m_lst.append((a, b))
    # print(m_lst)
    
    Long = -21e8
    for i in range(N):
        for j in range(N):
            back = copy.deepcopy(arr)
            for k in range(1,K+1):
                arr[i][j] -= k
                Long = max(Long, bfs(arr))
                arr = copy.deepcopy(back)
                
    print(f'#{tc} {Long}')