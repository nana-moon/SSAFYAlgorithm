# [[0,1,0],[1,1,1],[1,0,0],[0,0,1]]  답: 96
# [[1,1,0],[0,1,0],[0,0,0],[0,0,0]] 답 :12
# [[1,1,1],[1,1,1],[1,1,1],[1,1,1]] 답: 193912

import copy

def solution(arr):
    st = []
    for i in range(4):
        for j in range(3):
            if arr[i][j] == 1:
                st.append([i,j])
                
    dy = [0,0,-1,1,-1,-1,1,1]
    dx = [-1,1,0,0,1,-1,-1,1]
    
    back = copy.deepcopy(arr)
    
    def dfs(y,x,level):
        nonlocal cnt
        if level >= 1:
            cnt += 1
            
        for i in range(8):
            ny,nx = dy[i]+y,dx[i]+x
            if not(0<=ny<4 and 0<=nx<3): continue
            if arr[ny][nx] == 0: continue
            arr[ny][nx] = 0
            dfs(ny,nx,level+1)
            arr[ny][nx] = 1
            
    cnt = 0
    for s in st:
        arr = copy.deepcopy(back)
        arr[s[0]][s[1]] = 0
        dfs(s[0],s[1],0)
        
    return cnt

arr = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
print(solution(arr))