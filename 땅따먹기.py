def solution(land):   #DP
    size=len(land)
    DP=[[0, 0, 0, 0] for _ in range(size)]

    for i in range(size):
        for j in range(4):
            if i==0:
                DP[i][j]=land[i][j]
                continue
            max_val=max(DP[i-1])
            visited=DP[i-1].index(max_val)
            if j==visited:
                DP[i-1][visited]=0
                DP[i][j]=max(DP[i-1])+land[i][j]
                DP[i-1][visited]=max_val
            else:
                DP[i][j]=max(DP[i-1])+land[i][j]

    return max(DP[-1])

def solution2(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])


land=[[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
