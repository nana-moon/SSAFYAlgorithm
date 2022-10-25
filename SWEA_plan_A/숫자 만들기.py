def calculate(lst):
    tmp = num[:]
    for i in range(1, N):
        if lst[i-1] == 0:
            tmp[i] = tmp[i-1] + tmp[i]
        elif lst[i-1] == 1:
            tmp[i] = tmp[i-1] - tmp[i]
        elif lst[i-1] == 2:
            tmp[i] = tmp[i-1] * tmp[i]
        elif lst[i-1] == 3:
            tmp[i] = int(tmp[i-1] / tmp[i])
    return tmp[N-1]

def dfs(n, k): # n: 선택된 원소의 개수, k: 총 원소의 개수
    global Max, Min
    if n == k:
        tmp2 = oper[:]
        result = calculate(tmp2)
        Max = max(Max, result)
        Min = min(Min, result)    
        return
    for i in range(n, k):
        oper[n], oper[i] = oper[i], oper[n]
        if (''.join(map(str, oper)), n) in used:
            oper[n], oper[i] = oper[i], oper[n]
            continue
        used.add((''.join(map(str, oper)), n))
        dfs(n+1, k)
        oper[n], oper[i] = oper[i], oper[n]
        
        
for tc in range(1, int(input())+1):
    N = int(input())
    tmp = list(map(int, input().split()))
    oper = []
    for i in range(4):
        for _ in range(tmp[i]):
            oper.append(i)

    num = list(map(int, input().split()))
    
    used = set()

    Min, Max = 21e8, -21e8
    dfs(0, N-1)
    # print(Max, Min)
    print(f'#{tc} {Max-Min}')