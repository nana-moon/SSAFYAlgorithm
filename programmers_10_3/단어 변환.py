def solution(begin, target, words):
    answer = 0
    N = len(begin)
    M = len(words)
    used = [False]*M
    
    def dfs(level, word):
        nonlocal answer, N, M, used
        if word == target:
            answer = level
            return
        for i in range(M):
            if used[i] == True: continue
            cnt = 0
            for j in range(N):
                if word[j] != words[i][j]:
                    cnt += 1
            if cnt == 1:
                used[i] = True
                dfs(level+1, words[i])
                used[i] = False
            
    dfs(0, begin)
    return answer
    
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]


answer = solution(begin, target, words)
print(answer)