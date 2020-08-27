def solution(n, computers):
    count=0
    i,j=0,1
    while True:
        if i==0 and j==n-1:
            count+=1
            break
        if computers[i][j]==1 and j+1<=n-1:
            i+=1
            j+=1
        elif computers[i][j]==1 and j+1>n-1 :
            i=0
        else:
            count+=1
            i=0
    return count

n1, c1=3, [[1,1,0], [1, 1, 0], [0, 0, 1]]
n2, c2=3, [[1,1,0], [1, 1, 1], [0, 1, 1]]

print(solution(n1, c1))
print(solution(n2, c2))
