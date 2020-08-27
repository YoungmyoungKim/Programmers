import heapq
#버틸 수 있는 날짜까지만 힙에 넣고 맥스힙으로 만들기
def solution_3(stock, dates, supplies, k):
    answer = 0
    heap=[]
    plan=list(reversed(list(zip(dates, supplies))))
    while(stock<k):

        while(len(plan)!=0 and plan[-1][0]<=stock):
                heapq.heappush(heap,-plan.pop()[1])

        stock+= -heapq.heappop(heap)
        answer+=1
    return answer

def solution_4(stock, dates, supplies, k):
    answer = 0
    idx=-1
    heap=[]
    while(stock<k):
        for i in range(idx+1, len(dates)):
            if dates[i]<=stock:
                heapq.heappush(heap,-supplies[i])
                idx=i
            else:
                break
        stock+= -heapq.heappop(heap)

        answer+=1
    return answer

s=4
d=[4,10,15]
sup=[20,5,10]
k=30
print(solution_3(s,d,sup,k))
print(solution_4(s,d,sup,k))
