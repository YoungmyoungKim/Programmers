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

print(solution(b, m))
