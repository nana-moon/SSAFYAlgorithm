# 적록색약
import copy

def check(y, x, lst):
    global cnt
    color = lst[y][x]
    
    for i in range(4):
        
        ny = dy[i] + y
        nx = dx[i] + x
        if 0<=ny<N and 0<=nx<N and used[ny][nx] == False:
            if lst[ny][nx] == color:
                used[ny][nx] = True
                check(ny,nx,lst)
    print(used)     
    
    for i in range(4):
        
        ny = dy[i] + y
        nx = dx[i] + x
        if 0<=ny<N and 0<=nx<N and used[ny][nx] == False:
            # if lst[ny][nx] != color:
            cnt += 1
            print(ny,nx)
            used[ny][nx] = True
            check(ny,nx,lst)
    
            # used[ny][nx] = False 브레이크 조건이 없을 땐 쓰면 안됨

N = int(input())
arr = [list(input()) for _ in range(N)]
n_arr = copy.deepcopy(arr)
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            n_arr[i][j] = 'R'
# n_arr = [
# ['A', 'A', 'R', 'B', 'B'], 
# ['R', 'R', 'R', 'B', 'B'],
# ['B', 'B', 'B', 'R', 'R'], 
# ['B', 'B', 'R', 'R', 'R'], 
# ['R', 'R', 'R', 'R', 'R']]
        
cnt = 1
dy = [0,0,1,-1]
dx = [1,-1,0,0]
used = [[False]*N for _ in range(N)]         
used[0][0] = True
check(0,0,arr)
print()

# print(n_arr)
n_cnt = cnt
cnt = 1
used = [[False]*N for _ in range(N)]         
used[0][0] = True
check(0,0,n_arr)
rg_cnt = cnt
print(n_cnt, rg_cnt)
for x in used:
    print(*x)