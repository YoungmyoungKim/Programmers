def solution(arr1, arr2):
    li=[]

    for i in range(len(arr1)):
        row=[]
        for j in range(len(arr2[0])):
            val=0
            for k in range(len(arr1[0])):
                val+=arr1[i][k]*arr2[k][j]
            row.append(val)
        li.append(row)
    return li

a1, a2=[[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]
b1, b2=[[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(a1, a2))
print(solution(b1, b2))

print(list(zip(*b1)))
