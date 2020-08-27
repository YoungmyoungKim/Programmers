from string import ascii_uppercase
def solution(msg):
    alpha_list=list(ascii_uppercase)
    dic=dict(zip(alpha_list, range(1, 27)))
    answer=[]
    visited=[]
    for i in range(len(msg)):
        if i in visited:
            continue
        hit=[]
        fail=[]
        for j in range(i+1, len(msg)+1):
            if msg[i:j] in dic.keys():
                hit.append(msg[i:j])
                visited.append(j-1)
            else:
                fail.append(msg[i:j])

        answer.append(dic[hit[-1]])
        if len(fail) != 0:
            dic[fail[0]]=len(dic)+1

    return answer

msg1="KAKAO"
msg2="TOBEORNOTTOBEORTOBEORNOT"
msg3="ABABABABABABABAB"

print(solution(msg1))
print(solution(msg2))
print(solution(msg3))
