import re
import itertools

def solution(expression):
    numbers=re.findall('\d+', expression)
    operands=re.findall('\D+', expression)
    perm=list(itertools.permutations(list(set(operands)), len(set(operands))))
    exp=[]
    for i, num in enumerate(numbers):
        if i==len(numbers)-1:
            exp.append(num)
        else:
            exp.append(num)
            exp.append(operands[i])
            
    ans=0
    for op in perm:
        temp=exp[:]
        for x in op:
            temp=CalNumbers(temp, x)
        ans=max(ans, abs(temp[0]))

    return ans

def CalNumbers(ex, op):
    idx=0
    stack=[]
    while idx<len(ex):
        if ex[idx] != op:
            stack.append(ex[idx])
            idx+=1
        else:
            num1=stack.pop()
            num2=ex[idx+1]
            val=eval(str(num1)+op+str(num2))
            stack.append(val)
            idx+=2

    return stack

e1="100-200*300-500+20"
e2="50*6-3*2"

print(solution(e1))
print(solution(e2))
