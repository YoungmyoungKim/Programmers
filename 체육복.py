
def solution(n, lost, reserve):
    answer=0
    students=[1]*n
    for i in range(len(reserve)):
        students[reserve[i]-1]+=1
    for i in range(len(lost)):
        students[lost[i]-1]-=1

    for idx, student in enumerate(students):
        if student==0:
            if idx==0 and students[idx+1]==2:
                students[idx]+=1
                students[idx+1]-=1
                continue
            if idx==len(students)-1 and students[idx-1]==2:
                students[idx]+=1
                students[idx-1]-=1
                continue
            if idx>0 and idx<len(students)-1:
                if students[idx-1]==2:
                    students[idx]+=1
                    students[idx-1]-=1
                    continue
                if students[idx+1]==2:
                    students[idx]+=1
                    students[idx+1]-=1

    for student in students:
        if student>=1:
            answer+=1
    return answer

n_1, lost_1, reserve_1=5, [2, 4], [1, 3, 5]
n_2, lost_2, reserve_2=5, [2, 4], [3]
n_3, lost_3, reserve_3=3, [3], [1]
n_4, lost_4, reserve_4=3, [2], [1,2]
print(solution(n_1, lost_1, reserve_1))
print(solution(n_2, lost_2, reserve_2))
print(solution(n_3, lost_3, reserve_3))
print(solution(n_4, lost_4, reserve_4))
