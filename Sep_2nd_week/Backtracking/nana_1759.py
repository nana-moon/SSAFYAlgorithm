# 암호 만들기
import sys
input = sys.stdin.readline

pass_len, C = map(int, input().split())
pass_element = list(input().rstrip().split())
pass_element.sort()

moem = list('aeiou')

used = [False]*C

def dfs(level, start):
    if level == pass_len:
        m_cnt, j_cnt = 0, 0
        result = []
        for i in range(C):
            if used[i]:
                result.append(pass_element[i])
                if pass_element[i] in moem:
                    m_cnt += 1
                else:
                    j_cnt += 1            
        if m_cnt >= 1 and j_cnt >= 2:
            
            print(*result,sep='')           
        return
    for i in range(start,C):
        used[i] = True
        dfs(level+1, i+1) # i+1 주의
        used[i] = False

dfs(0,0)