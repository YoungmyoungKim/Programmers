import math
def solution(n,a,b):
    rivals=sorted([a, b])
    groups=[[x, x+1] for x in range(1, n, 2)]
    count=1
    while len(groups)>0:
        if rivals in groups:
            return count
        groups=match(groups, rivals)
        count+=1

def match(groups, rivals):
    teams=[[] for _ in range(len(groups)//2)]
    for i, group in enumerate(groups):
        if group[0] not in rivals and group[1] not in rivals:
            teams[i//2].append(group[0])
        elif group[0] in rivals:
            teams[i//2].append(group[0])
        else:
            teams[i//2].append(group[1])
    return teams

def solution2(n, a, b):
    count=0
    while a != b:
        a, b=math.ceil(a/2), math.ceil(b/2)
        count+=1
    return count
n, a, b=8, 4, 7

print(solution2(n, a, b))
