import math
import itertools

def is_Prime(number):
    if number<=1:
        return False
    else:
        for i in range(2, int(number**0.5)+1):
            if number%i==0:
                return False
        return True


def solution_2(numbers):     ##정답
    answer=0
    nums=list(numbers)
    p=[]
    for i in range(1,len(nums)+1):
        temp=list(map(''.join, itertools.permutations(numbers, i)))
        p+=temp
    p=list(set(map(int, p)))
    for number in p:
        if is_Prime(number)==True:
            answer+=1
    return answer

n1="17"
n2="011"

print(solution_2(n1))
print(solution_2(n2))
