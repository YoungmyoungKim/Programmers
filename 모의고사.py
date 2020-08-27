def solution(answers):
    answer = []
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[3,3,1,1,2,2,4,4,5,5]
    n_p1, n_p2, n_p3=0, 0, 0

    for i in range(1,len(answers)+1):
        x=p1[i%5-1]
        y=p2[i%8-1]
        z=p3[i%10-1]

        if x==answers[i-1]:
            n_p1+=1
        if y==answers[i-1]:
            n_p2+=1
        if z==answers[i-1]:
            n_p3+=1
    re=[n_p1, n_p2, n_p3]

    for i,v in enumerate(re):
        if v==max(re):
            answer.append(i+1)
        answer.sort()
    return answer

a1=[1,2,3,4,5]
a2=[1,3,2,4,2]

print(solution(a1))
print(solution(a2))
