def solution(n):
    numbers=DeciToBinary(n)
    n_count=0
    for number in numbers:
        if number==1:
            n_count+=1
    i=1
    while True:
        num_list=DeciToBinary(n+i)
        count=0
        for num in num_list:
            if num==1:
                count+=1
        if count==n_count:
            return n+i
        else:
            i+=1


def DeciToBinary(number):
    s=[]
    if number==1:
        return [1]
    while number != 0:
        s.append(number%2)
        number= number//2
    return list(reversed(s))

def solution2(n):
    count=bin(n).count('1')
    i=1
    while True:
        new_count=bin(n+i).count('1')
        if new_count==count:
            return n+i
        else:
            i+=1
    

n1=78
n2=15

print(solution2(n1))
print(solution2(n2))
