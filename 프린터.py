def solution(priorities, location):
    count=0
    priorities=[(y, x) for x, y in enumerate(priorities)]
    while len(priorities)>0:
        if priorities[0][0] < max(priorities)[0]:
            priorities.append(priorities[0])
        else:
            count+=1
            if priorities[0][1]==location:
                return count
        priorities.pop(0)


p1, l1=[2,1,3,2], 2
p2, l2=[1, 1, 9, 1, 1, 1], 0
p3, l3=[1, 1, 9, 1, 1, 1], 5


print(solution(p1, l1))
print(solution(p2, l2))
print(solution(p3, l3))
