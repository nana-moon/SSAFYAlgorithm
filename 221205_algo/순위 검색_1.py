from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(infos, querys):
    
    answer = []
    dic = defaultdict(list)
    for info in infos:
        info_lst = info.split()
        select_lst = info_lst[:-1] # 4가지
        score = info_lst[-1]
        for i in range(5): 
            combination = list(combinations(select_lst, i))
            for com in combination:
                key = ''.join(com)
                dic[key].append(int(score))
    
    for k, v in dic.items():
        dic[k].sort()

    for query in querys:
        query_lst= query.replace("-", "").replace("and", "").split()
        target = int(query_lst[-1])
        target_key = ''.join(query_lst[:-1])
        if target_key in dic.keys():
            answer.append(len(dic[target_key])-bisect_left(dic[target_key], target))
        else:
            answer.append(0)
        # print(str)
    # print(answer)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])