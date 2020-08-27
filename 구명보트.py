def solution(people, limit):
    count=0
    people.sort(reverse=True)
    onBoard=[]
    temp=[]
    j=-1
    for person in people[:]:
        temp.append(person)
        onBoard.append(person)
        while True:
            if len(onBoard)==len(people):
                 break
            if sum(temp)+people[j]<=limit:
                temp.append(people[j])
                onBoard.append(people[j])
                j-=1
            else:
                break
        count+=1
        temp=[]
        if len(onBoard)==len(people):
             break

    return count

p1, l1=[70, 50, 80, 50], 100
p2, l2=[70, 80, 50], 100
p3, l3=[90, 80, 70, 60, 50, 40], 120

print(solution(p1, l1))
print(solution(p2, l2))
print(solution(p3, l3))
