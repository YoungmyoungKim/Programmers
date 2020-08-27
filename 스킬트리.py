def solution(skill, skill_trees):
    answer = 0
    order=list(skill)
    for tree in skill_trees:
        temp=[]
        for item in tree:
            if item in skill:
                temp.append(item)
        for i in range(len(order)+1):
            if order[:i]==temp:
                answer+=1
                break
    return answer

skill, skill_trees= "CBD", ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))
