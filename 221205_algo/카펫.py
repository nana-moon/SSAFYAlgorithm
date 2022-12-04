def solution(brown, yellow):
    total = yellow + brown
    
    col, row = 2, 21e8
    answer = []
    
    for col in range(2, total):
        # 나머지가 0일 
        if total % col == 0:
            row = total // col
            if col <= row:
                if brown == (2*col) + (2*row) - 4:
                    answer = [row, col]
                    break
                    
        else:
            continue
            
    return answer

print(solution(24,24))