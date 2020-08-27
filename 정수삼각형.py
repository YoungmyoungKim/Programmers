def solution(triangle):
    table=[[-1 for _ in range(i+1)] for i in range(len(triangle))]
    for i in range(len(triangle)):
        for j in range(i+1):
            if i==0 and j==0:
                table[i][j]=triangle[i][j]
            elif j==0 :
                table[i][j]=table[i-1][j] + triangle[i][j]

            elif j==i :
                table[i][j]=table[i-1][j-1] + triangle[i][j]

            else:
                table[i][j]=max(table[i-1][j-1], table[i-1][j])+triangle[i][j]
    return max(table[-1])

t=[[7], [3,8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(t))
