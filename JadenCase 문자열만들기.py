def solution(s):
    s_li =s.split(" ")

    for i,ch in enumerate(s_li):
        if len(ch)<1:
            continue
        s_li[i]=ch[0].upper()+ch[1:].lower()

    return ' '.join(s_li)

def solution2(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])

s1="3people unFollowed me"
s2="for the last week"
s3="hello   my friend"

print(solution2(s1))
print(solution2(s2))
print(solution2(s3))
