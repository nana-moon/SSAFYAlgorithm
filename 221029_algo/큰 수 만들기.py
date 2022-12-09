def solution(number, k):
    result = [number[0]]
    for i in range(1, len(number)):
        while result and k > 0:
            # 앞 뒤 비교했을 때 뒤가 더 크면 앞의 값을 삭제
            if number[i] > result[-1]:
                result.pop()
                k -= 1
            else: break
        result.append(number[i])
    
    if k != 0:
        n = len(result)
        result = result[:n-k]
    answer = ''.join(result)
    return answer
