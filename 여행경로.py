def solution(tickets):
    dic={}
    for ticket in tickets:
        if ticket[0] in dic:
            dic[ticket[0]].append(ticket[1])
            dic[ticket[0]].sort(reverse=True)
        else:
            dic[ticket[0]]=[ticket[1]]

    path=[]
    stack=['ICN']
    while stack:
        node=stack[-1]
        if node not in dic or len(dic[node])==0:
            path.append(stack.pop())
        else:
            stack.append(dic[node].pop())
    path.reverse()
    return path



tickets1=[['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
tickets2=[['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
tickets3=[['ICN', 'AAA'], ['ICN', 'BBB'], ["BBB", "ICN"]]
ans=['ICN', 'BBB', 'ICN', 'AAA']
print(solution(tickets1))
print(solution(tickets2))
print(solution(tickets3))
