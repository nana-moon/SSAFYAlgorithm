from collections import deque
 
def bfs(y,x):
    global cnt
    q = deque([(y,x,1)])
    cnt += 1
    used[y][x] = True
    # (우, 하, 좌, 상), (하, 상), (우, 좌), (상, 우), (하, 우), (하, 좌), (상, 좌)
    direct = [[(0,1), (1,0), (0,-1),(-1,0)], [(1,0), (-1,0)], [(0,1), (0,-1)], [(-1,0), (0,1)], [(1,0), (0,1)], [(1,0), (0,-1)], [(-1,0), (0,-1)]]
    while q:
        yy, xx, level = q.popleft()
        if level == L:
            break
        dir_arr1 = direct[arr[yy][xx]-1][:]
        for i in range(len(dir_arr1)):
            ny = dir_arr1[i][0] + yy
            nx = dir_arr1[i][1] + xx
            # print('전',ny,nx)
            if not (0<=ny<N and 0<=nx<M): continue
            if used[ny][nx] == True: continue
            if arr[ny][nx] == 0: continue
            # 둘이 연결 되어 있을 때만 append
            # print('후',ny,nx)
            dir_arr2 = direct[arr[ny][nx]-1][:]
            for j in range(len(dir_arr2)):
                if (yy, xx) ==  (dir_arr2[j][0]+ny, dir_arr2[j][1]+nx):
                    cnt += 1
                    used[ny][nx] = True
                    q.append((ny,nx,level+1))
    return cnt
 
for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split()) # 세로, 가로, 맨홀Y, 맨홀X, 소요 시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [[False]*M for _ in range(N)]
 
    cnt = 0
    print(f'#{tc} {bfs(R,C)}')