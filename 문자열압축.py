def compress(s, tok_len):
    words=[s[i:i+tok_len] for i in range(0, len(s), tok_len)]
    target_string=''
    res=''
    count=0
    for word in words:
        if word != target_string:
            if count > 1:
                res += str(count)
            res += target_string
            target_string=word
            count=1
        else:
            count+=1
    if count == 1 :
        res+=target_string
    else:
        res += (str(count) + target_string)

    return len(res)

def solution_ym(s):
    min=len(s)
    for i in range(1, len(s)//2+1):
        temp_len = compress(s, i)
        if min > temp_len:
            min=temp_len
    return min

s1="aabbaccc"
s2="ababcdcdababcdcd"
s3="abcabcdede"
s4="abcabcabcabcdededededede"
s5="xababcdcdababcdcd"

#print(compress(s1, 1))
#print(compress(s2, 8))

print(solution_ym(s1))
print(solution_ym(s2))
print(solution_ym(s3))
print(solution_ym(s4))
print(solution_ym(s5))
