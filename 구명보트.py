def solution(people, limit):
    count=0
    weights=sorted(people, reverse=True)
    vote=[]
    for i in range(len(people)):
        if limit - weights[i] < 40:
            count+=1
            weights[i]=0
            continue

    if len(vote) != 0:
        count+=1

    return weights

p1, l1=[70, 50, 80, 50], 100
p2, l2=[70, 80, 50], 100
p3, l3=[90, 80, 70, 60, 50, 40], 120

print(solution(p1, l1))
print(solution(p2, l2))
print(solution(p3, l3))
