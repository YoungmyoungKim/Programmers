from itertools import combinations
def solution(numbers, K):
    li=[i for i in range(len(numbers))]
    min_swap=0

    for i in range(len(numbers)//2):
        pairs=list(combinations(li, 2))

    while len(li) != 0:
        print(li)
        pairs
        for i in range(len(pairs)):
            temp_nums=swap(temp_nums, pairs[i][0], pairs[i][1])
            li.remove(pairs[i][0])
            li.remove(pairs[i][1])
            min_swap+=1
        for n1, n2 in zip(temp_nums, temp_nums[1:]):
            if abs(n1-n2) > K:
                break
            return min_swap
    return -1

def swap(numbers, i, j):
    temp=numbers[i]
    numbers[i]=numbers[j]
    numbers[j]=temp
    return numbers

n1=[10, 40, 30, 20]
k1=20
n2=[3, 7, 2, 8, 6, 4, 5, 1]
k2=3

#print(solution(n1, k1))
print(solution(n2, k2))
