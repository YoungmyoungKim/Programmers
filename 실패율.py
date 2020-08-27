def solution(N, stages):
    answer = []

    for i in range(1, N+1):
        fail=len([x for x in stages if x==i])
        arrived=len([x for x in stages if x>=i])
        
        answer.append((i, fail/arrived if arrived != 0 else 0))
    answer.sort(key= lambda x: x[1], reverse=True)

    return [x for x, y in answer]

n1, stage1=5, [2, 1, 2, 6, 2, 4, 3, 3]
n2, stage2=4, [4,4,4,4,4]

print(solution(n1, stage1))
print(solution(n2, stage2))
