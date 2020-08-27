import math
def solution(progresses, speeds):
    answer = []
    terms=list(map(lambda x: math.ceil((100-x[0])/x[1]), zip(progresses, speeds)))
    terms.reverse()
    top=terms[-1]
    count=0

    while len(terms)>0:
        if terms[-1]<=top:
            terms.pop()
            count+=1
        else:
            answer.append(count)
            count=0
            top=terms[-1]
    answer.append(count)

    return answer

p, s=[93, 30, 55], [1, 30, 5]
print(solution(p,s))
