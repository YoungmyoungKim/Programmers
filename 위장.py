def solution(clothes):
    keys=[y for (x, y) in clothes]
    dic=dict()
    answer=1
    for key in set(keys):
        dic[key]=keys.count(key)

    for v in dic.values():
        answer*=(v+1)
    return answer-1

from functools import reduce
from collections import Counter
def solution_2(clothes):
    dic=Counter([key for value, key in clothes])
    #reduce(func, iterable, initializer(optional))
    answer=reduce(lambda x, y: x*(y+1), dic.values(), 1)-1
    return answer

c1=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban","headgear"]]
c2=[["crow_mask","face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution_2(c1))
print(solution_2(c2))
