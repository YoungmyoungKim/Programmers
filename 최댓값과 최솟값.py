def solution(s):
    numbers=list(map(int, s.split(' ')))
    max_num=max(numbers)
    min_num=min(numbers)
    return str(min_num)+" "+str(max_num)

s1='1 2 3 4'
s2='-1 -2 -3 -4'
s3='-1 -1'

print(solution(s1))
print(solution(s2))
print(solution(s3))
