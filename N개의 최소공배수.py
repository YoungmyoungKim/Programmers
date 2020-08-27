from math import gcd
def solution(arr):
    i=1
    max_val=max(arr)
    pre_max=-1
    while True:
        val=max_val*i
        count=0
        for num in arr:
            if val%num == 0:
                count+=1
        if count==len(arr):
            return val
        else:
            i+=1

def solution2(arr):
    def lcm(num1, num2):
        return num1*num2//gcd(num1, num2)
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr)==1:
            return arr[0]


a1=[2, 6, 8, 14]
a2=[1, 2, 3]

print(solution2(a1))
print(solution2(a2))
