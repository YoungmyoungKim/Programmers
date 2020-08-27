def solution(N, number):
    answer = -1    #최솟값이 8보다 크면 -1을 리턴하기 때문
    DP=[]

    for i in range(1, 9):
        num_set={ int(str(N)*i) }   #중복 제거를 위해 set 사용

        for j in range(i-1):
            for x in DP[j]:
                for y in DP[-j-1]:
                    num_set.add(x+y)
                    num_set.add(x-y)
                    num_set.add(x*y)

                    if y != 0:
                        num_set.add(x//y)
        if number in num_set:
            return i

        DP.append(num_set)

    return answer

N1, num1=5, 12
N2, num2=2, 11

print(solution(N1, num1))
print(solution(N2, num2))
