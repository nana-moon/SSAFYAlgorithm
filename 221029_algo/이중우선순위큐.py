import heapq 

def solution(operations):

    heap = []
    for i in range(len(operations)):
        oper, num = operations[i].split()
        if oper == 'I':
            heapq.heappush(heap, int(num))
        else:
            if heap: ### 요소가 남았는지 확인
                if num == '1': # 최댓값 삭제
                    heap.remove(heapq.nlargest(1, heap)[0])      
                else: # 최솟값 삭제
                    heapq.heappop(heap)
    if heap:
        answer = [heapq.nlargest(1, heap)[0], heap[0]]
    else:
        answer = [0, 0]

    return answer

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))