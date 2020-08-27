def solution(number, k):
    numbers=list(number)

    for i in range(k):
        for j, num in enumerate(numbers):
            if num < numbers[j+1]:
                numbers.remove(num)
                break
    answer=''.join(numbers)

    return answer

def solution_2(number, k):
    numbers=list(number)
    count=0
    max_idx=0
    start=1
    while(count<k):
        for i in range(start, len(numbers)):
            if numbers[i-1] < numbers[i]:
                max_idx=i
            elif numbers[i-1]>= numbers[i]:
                for j in range(min_idx, max_idx):
                    del numbers[j]
                    count+=1
                min_idx=i
                max_idx=i

    answer=''.join(numbers)
    return answer

def solution_3(number, k):
    numbers=list(number)

    for i in range(k):
        for j in range(len(numbers)-1):
            if numbers[j] < numbers[j+1]:
                del numbers[j]
                break
    answer=''.join(numbers)

    return answer

def solution_4(number, k):
    numbers=list(number)
    start=0
    re_idx=[]
    for i in range(k):
        for j in range(start, len(numbers)-1):
            if numbers[j] < numbers[j+1]:
                re_idx.append(j)
                start=j+1
                break

    answer=''.join(numbers)

    return re_idx

def solution_5(number, k): #시간초과
    numbers=list(number)
    count=0
    while count<k:
        for i in range(len(numbers)-1):
            if numbers[i] < numbers[i+1]:
                del numbers[i]
                count+=1
                break
            elif i==len(numbers)-2 and numbers[i] >= numbers[i+1]:
                numbers.pop()
                count+=1

    answer=''.join(numbers)

    return answer

def solution(number, k):   #최종
    numbers=list(number)
    count=0
    stack=[numbers[0]]
    for number in numbers[1:]:
        while count < k and len(stack) != 0 and stack[-1] < number:
            stack.pop()
            count+=1
        stack.append(number)

    if count<k:
        stack.pop()

    return ''.join(stack)



num1, k1='1924', 2
num2, k2='1231234', 3
num3, k3='4177252841', 4
num4, k4="1010", 2
'''
print(solution(num1, k1))
print(solution(num2, k2))
print(solution(num3, k3))
'''
'''
print(solution_3(num1, k1))
print(solution_3(num2, k2))
print(solution_3(num3, k3))
print(solution_3(num4, k4))
'''
"""
print(solution_4(num1, k1))
print(solution_4(num2, k2))
print(solution_4(num3, k3))
print(solution_4(num4, k4))
"""
print(solution_6(num1, k1))
print(solution_6(num2, k2))
print(solution_6(num3, k3))
print(solution_6(num4, k4))
