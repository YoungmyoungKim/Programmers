from functools import reduce
def solution(bridge_length, weight, truck_weights):
    current_time=1
    passing=[(truck_weights[0], current_time)]
    for truck_weight in truck_weights[1:]:
        #print(passing)
        passing_weight=reduce(lambda x,y: x+y, map(lambda x: x[0], passing))

        while (len(passing) == bridge_length or
         passing_weight+truck_weight>weight):
            if (bridge_length-(current_time-passing[0][1])-1) > 0:
                current_time+=(bridge_length-(current_time-passing[0][1])-1)
            passing_weight-=passing[0][0]
            del passing[0]

        current_time+=1
        passing.append((truck_weight, current_time))
        #print(passing)

    #print(passing)
    return current_time+bridge_length

b1, w1, t_w1=2, 10, [7,4,5,6]
b2, w2, t_w2=100, 100, [10]
b3, w3, t_w3=100, 100, [10,10,10,10,10,10,10,10,10,10]

print(solution(b1, w1, t_w1))
print(solution(b2, w2, t_w2))
print(solution(b3, w3, t_w3))
