def solution(inputString):
    stack=[]
    brackets=['(', ')', '{', '}', '[', ']', '<', '>']
    for val in inputString:
        if val in brackets:
            stack.append(val)

    return stack


in1='Hello World!'
in2='line [plus]'
in3='if(Count of eggs is 4.){Buy milk.}'
in4='>_<'

print(solution(in1))
print(solution(in2))
print(solution(in3))
print(solution(in4))
