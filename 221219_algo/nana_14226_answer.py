# 이모티콘 > BFS
from collections import deque
S = int(input())
q = deque()
used = list()
q.append([1,0,0])
used.append('1_0')
while q:
    cnt, clip, time = q.popleft()
    if cnt == S:
        print(time)
        break
    for i in range(3):
        if i == 0: # 복사
            new_cnt, new_clip, new_time = cnt, cnt, time+1
        elif i == 1 and clip != 0: # 붙여넣기
            new_cnt, new_clip, new_time = cnt + clip, clip, time+1
        elif i == 2 and cnt-1 > 0:
            new_cnt, new_clip, new_time = cnt-1, clip, time+1
        tmp = []
        tmp.append(str(new_cnt))
        tmp.append(str(new_clip))

        
        Str = '_'.join(tmp)
        if Str not in used:
            q.append([new_cnt, new_clip, new_time])
            used.append(Str)
    # print(used)
    # print(q)
            
        
            
