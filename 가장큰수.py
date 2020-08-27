from functools import reduce
def solution(numbers):
    num=map(str, sorted(numbers, key = lambda x: str(x)*3, reverse=True))
    return str(int(''.join(num)))

n1=[6,10,2]
n2=[3,30,34,5,9]
n3=[0,0,0,0,0]

print(solution(n1))
print(solution(n2))
print(solution(n3))

#앞자리가 같을때 뒷자리 숫자가 크면 앞으로, 작으면 뒤로
