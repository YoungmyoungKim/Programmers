def solution(name):
    answer=0
    iname=AlphabetToNum(name)
    zero_count=0  #A가 연속으로 나오는 길이를 구해서 빼기 

    for i, num in enumerate(iname):
        answer+= min(abs(num), abs(num-26))
        if num==0:
            zero_count+=1

    return answer+len(iname)-1-zero_count

def AlphabetToNum(name):
    ret=[]
    for ch in name:
        ret.append(ord(ch)-65)
    return ret


n1="JEROEN"
n2="JAN"


print(solution(n1))
print(solution(n2))
