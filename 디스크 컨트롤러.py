import heapq
def solution(jobs):
    temp_jobs=[]
    heapq.heapify(jobs)
    num_jobs= len(jobs)
    job=heapq.heappop(jobs)
    current_time=job[0]+job[1]

    sum=current_time-job[0]
    for i in range(num_jobs-1):
        while len(jobs)!=0 and jobs[0][0]<current_time:
            job=heapq.heappop(jobs)
            heapq.heappush(temp_jobs, (job[1],job[0]))

        if len(temp_jobs)==0:
            job=heapq.heappop(jobs)
            current_time+=(job[0]-current_time+job[1])
            sum+=job[1]
        else:
            job=heapq.heappop(temp_jobs)
            current_time+=job[0]
            sum+=(current_time-job[1])

    return sum//num_jobs   #소수점 이하 버림!!

j=[[0,3], [1,9], [2,6]]
print(solution(j))
