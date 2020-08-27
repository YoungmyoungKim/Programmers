def solution(s):
    s=sorted(s[2:-2].split("},{"), key= lambda x : len(x))

    li=[]
    for ch in s:
        ch=ch.split(',')
        for n in ch:
            if n != ',' and int(n) not in li:
                li.append(int(n))
    return li

import re
from collections import Counter
def solution2(s):
    s=Counter(re.findall('\d+', s))
    return list(map(int, [x for x, y in sorted(s.items(), key=lambda x : x[1], reverse= True)]))

s1="{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2="{{1,2,3},{2,1},{1,2,4,3},{2}}"
s3="{{20,111},{111}}"
s4="{{123}}"
s5="{{4,2,3},{3},{2,3,4,1},{2,3}}"

print(solution2(s1))
print(solution2(s2))
print(solution2(s3))
print(solution2(s4))
