def solution(n):
    if n<3:
        return str(n)
    elif n==3:
        return str(4)
    else:
        if n%3==0:
            return solution((n//3)-1) + solution(3)
        return solution(n//3)+solution(n%3)

n1=1
n2=2
n3=3
n4=4
n5=7
n6=15

print(solution(n1))
print(solution(n2))
print(solution(n3))
print(solution(n4))
print(solution(n5))
print(solution(n6))
