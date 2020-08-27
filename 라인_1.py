
def solution(inputString):
    brackets=['(', '{', '[', '>']
    li=[]
    for i, val in enumerate(inputString):
        if val in brackets:
            li.append(i)
    count=0
    for i in li:
        if ((inputString[i]=='(' and inputString.find(')', i) !=-1) or
        (inputString[i]=='{' and inputString.find('}', i) != -1) or
        (inputString[i]=='[' and inputString.find(']', i) != -1) or
        (inputString[i]=='<' and inputString.find('>', i) != -1) ):
            count+=1
        else:
            return -1

    return count


in1='Hello World!'
in2='line [plus]'
in3='if(Count of eggs is 4.){Buy milk.}'
in4='>_<'

print(solution(in1))
print(solution(in2))
print(solution(in3))
print(solution(in4))


#문제
'''
일상에서 괄호는 순서를 표현하거나, 부가 정보를 제공하거나, 특정 내용을 부각하는 등의 용도로 사용됩니다.
괄호는 여는 괄호와 닫는 괄호가 한 묶음을 이루어야 하는 특징을 가지고 있으며 다양한 괄호가 존재합니다.
아래의 규칙에 맞추어 임의의 문자열에 대해 다양한 괄호가 올바르게 사용되었는지 확인할 수 있는 해결법을 제시해 봅시다.

제한 사항
임의의 문자열 inputString이 입력됩니다
공백으로만 이루어진 문자열은 입력되지 않습니다
입력 문자열의 길이는 1 이상입니다
최대 길이는 명시되지 않습니다
괄호들이 정상적으로 사용되었는지 검증한 결과를 반환합니다
괄호는 아래와 같이 네 종류가 있다고 가정합니다
( ), { }, [ ], < >
괄호의 여닫는 특징만을 검증하며, 열려 있는 어떤 괄호에 대해서 짝이 다른 닫히는 괄호에 영향을 주지 않습니다
예를 들어 ([])와 ([)] 모두 잘 열고 잘 닫았기 때문에 정상입니다
정상이라면 총 괄호 쌍의 수, 비정상(괄호 쌍이 정상적인 순서로 표현되지 않은 경우)이라면 -1을 반환합니다

입출력 예
inputString	result
Hello, world!	0
line [plus]	1
if (Count of eggs is 4.) {Buy milk.}	2
>_<	-1
'''
