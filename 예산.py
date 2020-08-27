
def solution(budgets, M):
    budgets.sort()
    high=budgets[-1]
    low=budgets[0]
    l=[]

    while high>=low:
        temp_budgets=[]
        mid=(high+low)//2
        for i, budget in enumerate(budgets):
            if budget>mid:
                temp_budgets.append(mid)
            else:
                temp_budgets.append(budgets[i])
        if sum(temp_budgets)>M:
            high=mid-1
        else:
            low=mid+1
            l.append((mid, sum(temp_budgets)))

    return max(l)[0]

def solution_2(budgets, M):
    budgets.sort()
    high=budgets[-1]
    low=budgets[0]
    answer=0
    if low > M//len(budgets):
        return M//len(budgets)

    while high>=low:
        sum=0
        mid=(high+low)//2

        for budget in budgets:
            if budget>mid:
                sum+=mid
            else:
                sum+=budget
        if sum>M:
            high=mid-1
        else:
            low=mid+1
            answer=mid

    return answer

#제출코드
def solution(budgets, M):
    # 0 ~ budgets[-1] ~ M
    high=max(budgets)
    low=0
    answer=0

    while high>=low:
        mid=(high+low)//2
        expect_budgets=sum(map(lambda x: x if x <= mid else mid, budgets))
        if expect_budgets>M:
            high=mid-1
        else:
            low=mid+1
            answer=mid
    return answer

b, m= [120, 110, 140, 150], 485

print(solution_2(b, m))
