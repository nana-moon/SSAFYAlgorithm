# 입국심사
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

judges = [int(input()) for _ in range(N)]

max_time = min(judges) * M
st, ed = 0, max_time
answer = 0

while st <= ed:
    if st == ed: 
        answer = st
        break
    mid = (st + ed) // 2
    cnt = 0
    flag = False # 최솟값 찾기 위함
    for i in range(N):
        cnt += mid // judges[i]
        if mid % judges[i] == 0:
            flag = True
    if cnt == M and flag == True: # 정확하게 일치
        answer = mid
        break
    if cnt < M:
        st = mid + 1
    else:
        ed = mid - 1
        if st > ed: # 만약 목표 인원보다 많이 심사 가능하지만 최소 시간일 때
            answer = mid
            break 
        
print(answer)
            