import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    Counter=0
    while(scoville[0]<K):
        if len(scoville)<=1:
            return -1
        New=heapq.heappop(scoville)+2*heapq.heappop(scoville)
        heapq.heappush(scoville,New)
        Counter+=1

    return Counter

s=[1,2,3,9,10,12]
k=7

print(solution(s,k))
