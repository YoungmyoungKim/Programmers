def solution(s):
    s=list(reversed(s))
    i=0
    stack=[s.pop()]
    while s:
        if len(stack) != 0 and stack[-1]==s[-1]:
            stack.pop()
            s.pop()
        else:
            stack.append(s.pop())
    return 0 if len(stack)>0 else 1

s1="baabaa"
s2='cdcd'

print(solution(s1))
print(solution(s2))
