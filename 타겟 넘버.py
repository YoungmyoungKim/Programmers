def solution(numbers, target):
    q=[]
    q.append(+numbers[0])
    q.append(-numbers[0])
    del numbers[0]
    for number in numbers:
        temp=[]
        while(len(q)>0):
            temp.append(q.pop())
        for num in temp:
            q.append(num+number)
            q.append(num-number)
    """
    answer=0
    for val in q:
        if val==target:
            answer+=1
    """
    return q.count(target)

n=[1,1,1,1,1]
t=3
print(solution(n,t))
