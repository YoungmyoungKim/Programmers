from itertools import permutations
from copy import deepcopy
def solution(baseball):
    answer=[]
    candidates=list(map(''.join, permutations([str(i) for i in range(1, 10)], 3)))
    for n_score in baseball:
        for candidate in deepcopy(candidates):
            if check_score(n_score, candidate) == False:
                candidates.remove(candidate)

    return len(candidates)

def check_score(score, number):
    candidate=list(number)
    num=list(str(score[0]))
    s, b= 0, 0
    for i in range(3):
        if num[i]==candidate[i]:
            s+=1
        elif candidate[i] in num:
            b+=1
    if s==score[1] and b==score[2]:
        return True

    return False



bb=[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(bb))
