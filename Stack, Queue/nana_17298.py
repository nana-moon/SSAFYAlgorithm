# 오큰수
# 1. 나의 원래 풀이였던 것
# que를 선언 맨 앞의 것을 pop하면서 확인
from collections import deque
import sys

n = int(sys.stdin.readline())
que = deque(map(int, sys.stdin.readline().split()))
# print(que)
result = []
for i in range(n):
    target = que.popleft()
    for next in que:
        if target < next:
            result.append(next)
            break       
    else:
        result.append(-1)
        
print(*result)

# # 2. 구글링해서 얻은 답변
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
# 오큰수를 못 찾을 경우를 위해 -1으로 초기값 설정
answer = [-1 for i in range(n)]

# 리스트를 하나씩 순회
for i in range(len(arr)):
    # stack에 있는 인덱스 들의 값이 그 차례 값보다 작으면 그 인덱스의 오큰수를 해당 차례 값으로 만들어줌 -> pop해서 미완성 오큰수 인덱스에서 제거
    # 뒤에서 부터 확인
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
        
    # stack에 있는 인덱스 들의 값이 그 차레 값보다 다 큰 경우 stack은 그대로 놔두고 해당 인덱스만 append 해준다
    stack.append(i)

print(*answer)

