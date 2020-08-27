def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer=0
    for i in range(len(A)):
        answer+=(A[i]*B[i])
    return answer
def solution2(A, B):

    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse=True)))


a1, b1=[1, 4, 2], [5, 4, 4]
a2, b2=[1, 2], [3, 4]

print(solution2(a1, b1))
print(solution2(a2, b2))
