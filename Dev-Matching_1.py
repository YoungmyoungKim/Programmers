def solution(p,s):
    locker=[-i for i in range(1, 10)]+[i for i in range(10)]
    counter=[]
    for i,j in zip(p, s):
        i, j=eval(i), eval(j)
        plus_key_idx=locker.index(j)
        minus_key_idx=locker.index(-j)
        minus_cur_idx=locker.index(-i)
        plus_cur_idx=locker.index(i)

        counter.append(min(abs(plus_cur_idx-plus_key_idx), abs(plus_cur_idx-minus_key_idx), abs(minus_cur_idx-plus_key_idx), abs(minus_cur_idx-minus_key_idx)))

    return sum(counter)

p1="82195"
p2="00000000000000000000"
s1="64723"
s2="91919191919191919191"

print(solution(p1, s1))
print(solution(p2, s2))
