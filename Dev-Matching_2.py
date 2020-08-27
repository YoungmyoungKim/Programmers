def go_to_NSWE(i, j, head,office):
    size=len(office)
    old_i=i
    old_j=j
    if head=="N":
        i=i-1 if i-1>=0 else i
    elif head=="S":
        i=i+1 if i+1<size else i
    elif head=="W":
        j=j-1 if j-1>=0 else j
    else:
        j=j+1 if j+1<size else j

    if office[i][j]==-1:
        return old_i, old_j
    return i, j

def solution(office, r, c, move):
    sum=office[r][c]
    office[r][c]=0
    cur_i, cur_j=r, c
    heads=["N", "E", "S", "W"]
    head_idx=0
    for step in move:
        if step=="go":
            cur_i, cur_j =go_to_NSWE(cur_i, cur_j, heads[head_idx], office)
            sum+=office[cur_i][cur_j]
            office[cur_i][cur_j]=0
        elif step=="right":
            head_idx=0 if (head_idx+1)>3 else head_idx+1

        else:
            head_idx=3 if head_idx-1 < 0 else head_idx-1
        #print(cur_i, cur_j, heads[head_idx], sum)
    return sum

office=[[5, -1, 4], [6, 3, -1], [2, -1, 1]]
r=1
c=0
move=["go","go","right","go","right","go","left","go"]

print(solution(office, r, c, move))
