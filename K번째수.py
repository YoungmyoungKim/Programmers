def solution(array, commands):
    answer = []

    for value in commands:
        list=[]
        for i in range(value[0]-1, value[1]):
            list.append(array[i])
        list.sort()
        answer.append(list[value[2]-1])

    return answerK

array=[1,5,2,6,3,7,4]
c=[[2,5,3], [4,4,1], [1,7,3]]

print(solution(array, c))
