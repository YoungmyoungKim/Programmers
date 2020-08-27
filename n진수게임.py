def solution(n, t, m, p):
    s=''
    i=0
    while len(s)<m*t+1:
        s+=CalNnumbers(n, i)
        i+=1
    re=[x for i, x in enumerate(s) if i%m==(p-1)]
    return ''.join(re[:t])

def CalNnumbers(n, num):
    numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    n_numbers=[x for i, x in enumerate(numbers) if i<n]
    s=[]
    while True:
        if num//n==0:
            s.append(str(n_numbers[num%n]))
            break
        else:
            s.append(str(n_numbers[num%n]))
            num=num//n
    return ''.join(reversed(s))



n1, t1, m1, p1=2, 4, 2, 1
n2, t2, m2, p2=16, 16, 2, 1
n3, t3, m3, p3=16, 16, 2, 2
print(solution(n1, t1, m1, p1))
print(solution(n2, t2, m2, p2))
print(solution(n3, t3, m3, p3))
