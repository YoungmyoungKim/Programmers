def solution(citations):
    n=len(citations)
    h=n
    citations.sort(reverse=True)
    while h>0:
        upper_h=citations[0:h]
        if upper_h[-1]>=h:
            return h
        h-=1
    return 0

c=[3,0,6,1,5]

print(solution(c))
