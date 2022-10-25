from collections import deque
import copy

def bfs(h,w,lst):                    
    q1 = deque([(h,w,lst[h][w])])
    lst[h][w] = 0
    broken = 1

    while q1:
        y,x,ran = q1.popleft()
        for j in range(1,ran):
            for i in range(4):
                ny = dy[i]*j + y
                nx = dx[i]*j + x
                if not(0<=ny<H and 0<=nx<W): continue
                if lst[ny][nx] == 0: continue
                if lst[ny][nx] != 1:
                    q1.append((ny,nx,lst[ny][nx]))  
                broken += 1
                lst[ny][nx] = 0
    return broken
    
def sorting(lst):
    # arr -> 밑으로 내려서 정리 해야 함
    for a in range(W):
        down = 0
        for b in range(H-1, -1, -1):
            if lst[b][a] == 0:
                down += 1
            elif lst[b][a] != 0:
                lst[b+down][a], lst[b][a] = lst[b][a],lst[b+down][a]
    
                
def dfs(arr, level, cnt):
    global Max
    if cnt == total:
        Max = cnt
        return
    if level == N:
        Max = max(Max, cnt)
        return
    for w in range(W):
        new_arr = copy.deepcopy(arr)
        for h in range(H):
            if new_arr[h][w] != 0:
                yy, xx = h, w
                result = bfs(yy,xx,new_arr)
                sorting(new_arr)
                dfs(new_arr, level+1, cnt+result)
                break

for tc in range(1, int(input())+1):
    N, W, H = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    total = 0 # 총 벽돌의 수
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 0: total += 1
    total = W*H-total
    # print(total)
    dy, dx = [0,0,1,-1], [1,-1,0,0]
    Max = 0
    dfs(arr, 0, 0)
    print(f'#{tc} {total-Max}')