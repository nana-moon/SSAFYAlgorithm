'''
def solution(numbers):
    result = []
    for i in range(len(numbers)):
        result.append(str(numbers[i]))
        for j in range(i, 0, -1):
            a, b = result[j-1], result[j] 
            if a+b < b+a:
                result[j],result[j-1]=result[j-1],result[j]
            else:
                break
    
    answer = str(int(''.join(result)))
    return answer
'''
from functools import cmp_to_key

def compare(x, y):
    if x+y < y+x:
        return 1 #나중에 들어온 요소가 앞으로 정렬됨
    else:
        return -1 # 위치 변화 없음
        

def solution(numbers):
    numbers = [str(num) for num in numbers]
    result = sorted(numbers, key = cmp_to_key(compare))
    return str(int(''.join(result)))

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))