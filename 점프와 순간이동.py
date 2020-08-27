def solution(n):
    if n==1:
        return 1
    elif n!=1 and n%2==0:
        return solution(n//2)
    else:
        return solution(n-1)+1

n1=5
n2=6
n3=5000

print(solution(n1))
print(solution(n2))
print(solution(n3))
