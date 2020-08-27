def solution(heights):
    answer = [0 for i in range(len(heights))]
    for i in reversed(range(len(heights))):
        if i==0:
            continue
        for j in reversed(range(i)):
            if heights[j]>heights[i]:
                answer[i]=j+1
                break
    return answer

def solution_1(heights):
    answer=[]
    stack=[]
    for i in heights:
        stack.append(i)
    



    return answer

h1=[6,9,5,7,4]
h2=[3,9,9,3,5,7,2]
h3=[1,5,3,6,7,6,5]


print(solution(h1))
print(solution(h2))
print(solution(h3))
