import sys

# 가르침
N, K = map(int, input().split())
words = [sys.stdin.readline().rstrip()[4:-4] for _ in range(N)]
# 최대 단어의 개수
Max = 0 

arr = 'antic'
new_arr = []
for word in words:
    for i in word:
        if i not in arr and i not in new_arr:
            new_arr.append(i)
# new_arr에서 K-5개를 뽑는다.
L = len(new_arr)
path = [0 for _ in range(L)]

def dfs(level, start):
    global Max
    
    if level == K-5:
        tmp = list('antic')
        for l in range(L):
            if path[l] == 1:
                tmp.append(new_arr[l])
        cnt = 0
        for word in words:
            flag = 1
            for w in word:
                if w not in tmp:
                    flag = 0
                    break
            if flag:
                cnt += 1
        Max = max(Max, cnt)
        return
    
    for i in range(start, L):
        path[i] = 1
        dfs(level+1, i+1)
        path[i] = 0
        
# 예외처리 필수        
if K-5 < 0:
    print(0)
elif 0 <= K-5 < L:
    dfs(0,0)
    print(Max)
else:
    print(N)