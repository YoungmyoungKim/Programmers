def solution_wj(s):
    min_length=len(s)

    for i in range(1, len(s)+1):
        pos=0
        target_string=""
        i_unit_length=0

        count = 1
        comp = ""
        while pos < len(s):

            #if s[pos:pos+i] != target_string:

            if count != 1:
                i_unit_length += len(str(count))
                comp = comp + str(count)
            i_unit_length += len(target_string)
            target_string = s[pos:pos+i]
            count = 0

            while s[pos:pos+i] == target_string and pos < len(s):
                pos += i
                count += 1

        if count != 1:
            i_unit_length += len(str(count))
        i_unit_length += len(target_string)

        if min_length > i_unit_length:
            min_length = i_unit_length

    return min_length

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
