def solution(heights):
    len_heights=len(heights)
    answer=[0 for _ in range(len_heights)]
    stack=[(heights[-1], 0)]
    heigts=heights[:-1]
    for i, height in enumerate(reversed(heights)):
        while len(stack) != 0 and stack[-1][0] < height:
            item=stack.pop()
            answer[item[1]]=len_heights-i
        stack.append((height, i))

    return list(reversed(answer))

h=[6,9,5,7,4]
print(solution(h))
#print()
