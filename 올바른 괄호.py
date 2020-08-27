def solution(s):
    sum=0
    for i in s:
        sum+=BracketToNum(i)
        if sum < 0:
            return False
    if sum == 0:
        return True
    return False

def BracketToNum(s):
    if s=='(':
        return 1
    else:
        return -1

s1="()()"
s2="(())()"
s3=")()("
s4="(()("

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
