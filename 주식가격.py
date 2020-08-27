def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[j] < prices[i]:
                break

    return answer

def solution2(prices):   #Queue
    answer = [0]*len(prices)
    stack=[(prices[0], 1)]

    for i, price in enumerate(prices[1:], start=2):
        while stack[-1][0] > price:
            item, idx=stack.pop()
            answer[idx-1]=i-idx
        stack.append((price, i))

    for p, i in stack:
        answer[i-1]=len(prices)-i

    return answer

p1=[1, 2, 3, 2, 3]

print(solution2(p1))
