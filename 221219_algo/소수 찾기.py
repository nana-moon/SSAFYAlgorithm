import itertools, math

def is_prime(number):
    if number in [0,1]: return False
    if number == 2: return True
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0: # 소수 아님
            return False
    return True


def solution(numbers):
    answer = 0
    num_lst = list(numbers)
    num_set = set()
    for i in range(1, len(numbers)+1):
        result = list(set(itertools.permutations(num_lst, i)))
        for j in range(len(result)):
            tmp = result[j]
            str = "".join(tmp)
            num = int(str)
            if num not in num_set:
                num_set.add(num)
                flag = is_prime(num)
                if flag:
                    answer += 1

    return answer


print(solution("011"))