import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    heap=[]
    heapq.heappush(heap, (0,stock))
    for i in range(len(dates)):
        heapq.heappush(heap, (dates[i], supplies[i]))
    heapq.heappush(heap,(k,0))

    length=len(heap)
    for i in range(0,length-1):
        d,s=heapq.heappop(heap)
        if d==0:
            print(stock)
            continue
        temp_stock=stock-d
        if temp_stock<(heap[0][0]-d):
            stock=temp_stock
            stock+=s
            answer+=1
        print(answer)
        print(heap)
    return answer

def solution_1(stock, dates, supplies, k):
    answer = 0
    heap=[]
    heapq.heappush(heap, (0,stock))
    for i in range(len(dates)):
        heapq.heappush(heap, (dates[i], supplies[i]))
    heapq.heappush(heap,(k,0))
    print(heap)
    length=len(heap)
    while(len(heap)>1):
        print('stock:'+str(stock))
        d,s=heapq.heappop(heap)
        if stock<heap[0][0]-d:
            stock+=s
            answer+=1
            print(stock)
        stock=stock-(heap[0][0]-d)

        print('stock:'+str(stock)+'answer:'+str(answer))
        print(heap)
    return answer

#버틸 수 있는 날짜까지만 힙에 넣고 맥스힙으로 만들기
def solution_2(stock, dates, supplies, k):    #런타임에러
    answer = 0
    idx=-1
    while(stock<k):
        heap=[]
        for i in range(idx+1, len(dates)):
            if dates[i]<=stock:
                heapq.heappush(heap,((-1)*supplies[i],i))
            else:
                break
        s,idx=heapq.heappop(heap)
        stock=stock+(-1)*s
        answer+=1
    return answer

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
print(solution_4(s,d,sup,k))
