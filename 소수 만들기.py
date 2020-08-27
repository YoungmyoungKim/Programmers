from itertools import combinations
def solution(nums):
    li=list(combinations(nums, 3))
    count=0
    for numbers in li:
        if isPrime(sum(numbers))==True:
            count+=1
    return count

def isPrime(number):
    for i in range(2, number//2+1):
        if number%i==0:
            return False
    return True


num1=[1, 2, 3, 4]
num2=[1, 2, 7, 6, 4]

print(solution(num1))
print(solution(num2))
