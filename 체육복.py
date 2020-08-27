def solution(n, lost, reserve):
    _reserve=[i for i in reserve if i not in lost]
    _lost=[i for i in lost if i not in reserve]

    for num in _reserve:
        r=num+1
        l=num-1
        if l in _lost:
            _lost.remove(l)
        elif r in _lost:
            _lost.remove(r)
    return n-len(_lost)
    
n_1, lost_1, reserve_1=5, [2, 4], [1, 3, 5]
n_2, lost_2, reserve_2=5, [2, 4], [3]
n_3, lost_3, reserve_3=3, [3], [1]
n_4, lost_4, reserve_4=3, [2], [1,2]
print(solution(n_1, lost_1, reserve_1))
print(solution(n_2, lost_2, reserve_2))
print(solution(n_3, lost_3, reserve_3))
print(solution(n_4, lost_4, reserve_4))
