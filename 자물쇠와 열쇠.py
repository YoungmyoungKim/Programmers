def solution(key, lock):
    answer = True
    return answer

def rotate_key(key):
    l=len(key)
    r_key=[ [] for _ in range(l)]

    for i in range(l):
        for j in range(l-1, -1, -1):
            r_key[i].append(key[j][i])
    return r_key

k1, l1=[[0, 0, 0],[1, 0, 0],[0, 1, 1]], [[1, 1, 1],[1, 1, 0],[1, 0, 1]]

print(rotate_key(k1))
