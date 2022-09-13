# 단지 번호 붙이기
# 총단지의 수와 각 단지에 속하는 집의 수를 출력

def dfs(y,x):
    global cnt
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0<= ny < N and 0<= nx < N:
            if visited[ny][nx] == False and arr[ny][nx] == '1':
                visited[ny][nx] = True
                cnt += 1
                dfs(ny,nx)
            

N = int(input())
arr = [list(input()) for _ in range(N)]

visited = [[False]*N for _ in range(N)]
num = 0 # 단지의 수
cnt_lst = [] # 단지의 개수 담는 리스트
dy = [0,0,1,-1]
dx = [1,-1,0,0]

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and visited[i][j] == False:
            cnt = 1
            num += 1
            visited[i][j] = True
            dfs(i,j) # 숫자, 개수
            cnt_lst.append(cnt)

cnt_lst.sort()
print(num)
print(*cnt_lst, sep = '\n')
