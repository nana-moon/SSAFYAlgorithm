from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    m = len(maps)
    n = len(maps[0])

    queue = deque()
    queue.append([0, 0])

    while queue:
        y, x = queue.popleft()
        # print(y,x)

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= ny < m and 0 <= nx < n): continue
            if maps[ny][nx] == 0: continue
            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append([ny, nx])

    if maps[-1][-1] == 1: return -1
    else: return maps[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))