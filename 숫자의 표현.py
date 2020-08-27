def solution(n):
    ret=0
    for i in range(1, n//2+1):
        ret+=SumfromN(i, n)
    return ret+1

def SumfromN(num1, num2):
    sum=0
    while sum<num2:
        sum+=num1
        if sum == num2:
            return 1
        num1+=1
    return 0

def solution2(n):
    sum=0
    for i in range(1, n+1, 2):
        if n%i==0:
            sum+=1
    return sum

n=15
print(solution2(n))
