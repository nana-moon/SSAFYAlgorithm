from collections import deque
import copy


def bfs1(total,arr):
    Min = total
    
    # origin = copy.deepcopy(arr)
    # tmp = copy.deepcopy(arr)
    q2 = deque([(total, arr, 0)])
    while q2:
        remain, tmp, level= q2.popleft() # 남은 벽돌의 수, 배열
        lst = copy.deepcopy(tmp)
        # print(lst)
        
        if level == 3:
            Min = min(Min, remain)
            
        ## 진입 안됨
        
        for w in range(W):            
            for h in range(H):
                # print(h,w)
                if lst[h][w] != 0:
                    # print(w)
                    
                    len = lst[h][w]-1
                    lst[h][w] = 0
                    cnt = 1
                    used = [[False]*W for _ in range(H)]
                    used[h][w] = True
                    
                    q1 = deque([(h,w,len)])
                
                    while q1:
                        y,x,ran = q1.popleft()
                        if ran == 0:
                            continue
                        for i in range(4):
                            for j in range(ran):
                                ny = dy[i]*j + y
                                nx = dx[i]*j + x
                                if not(0<=ny<H and 0<=nx<W): continue
                                if used[ny][nx] == True: continue
                                if lst[ny][nx] == 0: continue
                                cnt += 1
                                used[ny][nx] = True
                                num = lst[ny][nx]-1
                                lst[ny][nx] = 0
                                q1.append((ny,nx,num))
                            
                    # if w == 1: print(cnt)
                    
                    if remain-cnt == 0:
                        return 0
                    
                    # arr -> 밑으로 내려서 정리 해야 함
                    for a in range(W):
                        down = 0
                        for b in range(H-1, -1, -1):
                            if lst[b][a] == 0:
                                down += 1
                            elif lst[b][a] != 0:
                                lst[b-down][a], lst[b][a] = lst[b-down][a], lst[b][a]
                    
                    
                    q2.append((remain-cnt, lst, level+1))
                    lst = copy.deepcopy(tmp)
                    
                    
                    break
                    
    return Min
                
def dfs(arr, level, cnt):
    global Max
    if level == N:
        Max = max(Max, cnt)
        return
    for w in range(W):
        new_arr = copy.deepcopy(arr)
        for h in range(H):
            if new_arr[h][w] != 0:
                yy, xx = h, w
                break
        result = bfs(yy,xx,new_arr)
        sort(new_arr)
        dfs(new_arr, level+1, cnt+result)
    
    

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
    print(dfs(arr, 0, 0))