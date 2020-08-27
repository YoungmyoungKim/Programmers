def solution_1(participant, completion):  #시간초과
    temp=participant
    for i in completion:
        if i in participant:
            temp.remove(i)
    answer = temp[0]
    return answer

def solution_2(participant, completion):    #근주힌트 but 시간초과
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            answer=participant[i]
    return answer

def solution_3(participant, completion):
    participant.sort()
    completion.sort()
    answer=participant[-1]
    for i in range(0,len(completion)):
        if participant[i]!=completion[i]:
            answer=participant[i]
            break
    return answer

participant_1=['leo', 'kiki', 'eden']
completion_1=['eden', 'kiki']

participant_2=['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion_2=['marina', 'josipa', 'nikola', 'filipa']

participant_3=['mislav', 'stanko', 'mislav', 'ana']
completion_3=['stanko','ana', 'mislav']
p=sorted(participant_3)
c=sorted(completion_3)
print(p)
print(c)
participant_3.sort()
completion_3.sort()
print(participant_3)
print(completion_3)
