from collections import deque

            

def solution(n, computers):
    used = [False]*n
    answer = 0
    
    def bfs(line):   
        q = deque()
        for j in range(n):
            if used[j] == False and j != line and computers[line][j] == 1:
                used[j] = True
                q.append(j)
                
        while q:
            node = q.popleft()
            for j in range(n):
                if used[j] == False and j != node and computers[node][j] == 1:
                    used[j] = True
                    q.append(j)  
                
    for i in range(n):
        if used[i] == False:
            bfs(i)
            answer += 1

    
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))