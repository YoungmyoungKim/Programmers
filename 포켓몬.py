def solution(nums):
    N=len(nums)
    if len(set(nums)) >= N//2:
        return N//2

    return len(set(nums))

num1=[3, 1, 2, 3]
num2=[3, 3, 3, 2, 2, 4]
num3=[3, 3, 3, 2, 2, 2]

print(solution(num1))
print(solution(num2))
print(solution(num3))
