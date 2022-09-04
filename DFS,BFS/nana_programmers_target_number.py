# 타겟 넘버
def solution(numbers, target):
    answer = 0
    length = len(numbers)
    stack = [[0,0]]
    visited = [False]*length
    
    while stack:
        sum, idx = stack.pop()
        if idx == length:
            if sum == target:
                answer += 1
        if idx < length and visited[idx] == False:
            visited[idx] = True
            stack.append([sum + numbers[idx], idx+1])
            stack.append([sum - numbers[idx], idx+1])

    return answer

numbers = list(map(int, input().split()))
target = int(input())
print(solution(numbers, target))