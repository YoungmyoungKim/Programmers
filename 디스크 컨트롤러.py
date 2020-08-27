import heapq
def solution(jobs):
    temp_jobs=[]
    n=len(jobs)
    jobs.sort(reverse=True)
    current_time=0
    sum=0
    while len(jobs)>0:
        if len(temp_jobs)!=0 and jobs[-1][0]>current_time:
            item=heapq.heappop(temp_jobs)
            current_time+=item[1]
            sum+=(current_time-item[0])
        elif len(temp_jobs)==0 and [-1][0]>current_time:
            item=jobs.pop()
            current_time+=(current_time-item[0]+item[1])
            sum+=(current_time-item[0])
        else:
            item=jobs.pop()
            item=[item[1], item[0]]
            heapq.heappush(temp_jobs, item)
    while len(temp_jobs)>0:
        item=heapq.heappop(temp_jobs)
        current_time+=item[0]
        sum+=(current_time-item[1])
    return sum/n

#요청이 겹치지 않는 경우 고려해야함.
#요청이 제일 빠른 것 시작
#실행 가능한 job들을 힙에 넣은 후 작은 것 부터 실행.

jobs=[[0,3], [1,9], [2, 6]]

print(solution(jobs))
