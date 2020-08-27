def solution(participant, completion):
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
