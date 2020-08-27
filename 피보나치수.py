def solution(n):
    answer = fib(n)%1234567
    return answer

def fib(n):
    li=[0, 1]
    for i in range(1, n):
        li.append(li[i-1]+li[i])
    return li[n]


n1=3
n2=5

print(solution(n1))
print(solution(n2))
