def solution(str1, str2):
    arr1, arr2=makeMulSet(str1, str2)
    inter=[]
    for val in arr1:
        if val in arr2:
            inter.append(val)
            arr2.remove(val)
    arr1.extend(arr2)
    union=arr1

    if len(inter)==0 and len(union)==0:
        return 65536
    return int(len(inter)/len(union)*65536)

def makeMulSet(str1, str2):
    li1=[str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    li2=[str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]
    return li1, li2

s11, s12="FRANCE","french"
s21, s22="shake hands","handshake"
s31, s32="aa1+aa2","AAAA12"
s41, s42="E=M*C^2","e=m*c^2"

print(solution(s11, s12))
print(solution(s21, s22))
print(solution(s31, s32))
print(solution(s41, s42))
