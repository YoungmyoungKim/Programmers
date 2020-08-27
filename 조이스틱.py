def solution(name):
    answer=0
    iname=AlphabetToNum(name)
    base=[0]*len(iname)
    i=0
    while True:
        if iname[i] != 0:
            answer+= min(abs(iname[i]), abs(iname[i]-26))
            iname[i]=0

        if iname==base:
            break
        else:
            for j in range(1, len(iname)):
                if iname[i+j] !=0:
                    i=i+j
                    answer+=j
                    break
                elif iname[i-j] !=0:
                    i=i-j
                    answer+=j
                    break

    return answer

def AlphabetToNum(name):
    ret=[]
    for ch in name:
        ret.append(ord(ch)-ord('A'))
    return ret


n1="JEROEN"
n2="JAN"


print(solution(n1))
print(solution(n2))
