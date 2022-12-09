def solution(progresses, speeds):
    stack = []
    answer = []
    for i in range(len(progresses)):
        
        sub = 100 - progresses[i]
        tmp = sub // speeds[i] 
        if sub % speeds[i] != 0:
            tmp += 1
        stack.append(tmp)
        
    cnt = 1
    core = stack[0]
    for i in range(1, len(stack)):
        if stack[i] <= core:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            core = stack[i]

    answer.append(cnt)

    return answer