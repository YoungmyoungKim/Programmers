def solution_1(bridge_length, weight, truck_weights):
    answer = 0
    passing=[]
    passed=[]
    trucks=[x for x in truck_weights]
    on_t=[0 for x in truck_weights]
    while(len(passed)<len(truck_weights)):
        if len(trucks)!=0:
            if sum(passing)+trucks[0]<=weight:
                passing.append(trucks[0])
                del trucks[0]
        print(passing)

        for i in range(len(passing)):
            if on_t[i]>=bridge_length:
                passed.append(passing[i])
                del passing[i]
            on_t[i]+=1
        answer=answer+1
        #print(on_t)
        #print(passed)

    #print(on_t)
    #print(passing)
    #print(passed)
    return answer

def solution_2(bridge_length, weight, truck_weights):
    answer = 0
    passed=[]
    passing=[0 for x in range(bridge_length)]
    trucks=[x for x in truck_weights]
    while(len(passed)<len(truck_weights)):
        if len(trucks)!=0 and sum(passing)+trucks[0]<=weight:
            passing.append(trucks[0])
            del trucks[0]
        else:
            passing.append(0)
        if passing[0]!=0:
            passed.append(passing[0])
        del passing[0]
        answer+=1
        print('passed:'+str(passed)+'passing:'+str(passing))
        #print('passed:'+str(passed))
    #answer=answer-2
    return answer

def solution_3(bridge_length, weight, truck_weights):
    answer = 0
    passed=[]
    passing=[0 for x in range(bridge_length)]
    trucks=[x for x in truck_weights]
    while(len(passed)<len(truck_weights)):
        if len(passing)>bridge_length:
            if passing[0]!=0:
                passed.append(passing[0])
            del passing[0]

        if len(trucks)!=0 and sum(passing)+trucks[0]<=weight:
            passing.append(trucks[0])
            del trucks[0]
        else:
            passing.append(0)
        answer+=1
        print('passed:'+str(passed)+'passing:'+str(passing))
        #print('passed:'+str(passed))
    #answer=answer-2
    return answer

def solution_4(bridge_length, weight, truck_weights):
    answer = 0
    passed=[]
    passing=[0 for x in range(bridge_length)]
    trucks=[x for x in truck_weights]
    while(len(passed)<len(truck_weights)):
        if len(trucks)!=0 and sum(passing)+trucks[0]<=weight:
            passing.append(trucks[0])
            del trucks[0]
        else:
            passing.append(0)

        if len(passing)>bridge_length:
            if passing[0]!=0:
                passed.append(passing[0])
            del passing[0]

        answer+=1
        print('passed:'+str(passed)+'passing:'+str(passing))

    #answer=answer-2
    return answer

from functools import reduce
def solution_5(bridge_length, weight, truck_weights):
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

print(solution_5(b1, w1, t_w1))
print(solution_5(b2, w2, t_w2))
print(solution_5(b3, w3, t_w3))
