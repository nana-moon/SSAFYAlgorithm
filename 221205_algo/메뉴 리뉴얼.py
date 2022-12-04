import itertools
def solution(orders, course):
    
    answer = []
    for cnt in course:
        all_combi = []
        for order in orders:
            all_combi.extend(list(itertools.combinations(sorted(order), cnt)))
        dic = {}
        
        Max = 0
        for combi in all_combi:
            str_combi = ''.join(combi)
            if str_combi in dic:
                dic[str_combi] += 1
                Max = max(Max, dic[str_combi])
            else:
                dic[str_combi] = 1
                
        if Max != 0 and Max != 1:
            for d in dic:
                if dic[d] == Max:
                    answer.append(d)

    return sorted(answer)