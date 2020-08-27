def solution(n, arr1, arr2):
    answer = []
    map=[]
    for x, y in zip(arr1, arr2):
        val=str(bin(x|y)[2:])
        val=val.rjust(n, '0')
        val=val.replace('1', '#')
        val=val.replace('0', ' ')
        map.append(val)
    return map

def NumToBinary(arr):
    li=[]
    for num in arr:
        s= str(bin(num))
        li.append(s[2:])

    return li

def binaryToMap(n, arr):
    for i, val in enumerate(arr):
        arr[i]=val.rjust(n, '0')
    return arr


n1, arr11, arr12=5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]
n2, arr21, arr22=6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]

print(solution(n1, arr11, arr12))
print(solution(n2, arr21, arr22))
