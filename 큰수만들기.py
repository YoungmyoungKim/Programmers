def solution(number, k):
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

print(solution(num1, k1))
print(solution(num2, k2))
print(solution(num3, k3))
