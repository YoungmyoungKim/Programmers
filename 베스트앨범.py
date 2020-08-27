from collections import defaultdict
def solution(genres, plays):
    streams=[(x[0], x[1], i) for i, x in enumerate(zip(genres, plays))]
    streams.sort(key= lambda x : x[1], reverse=True)
    count_dic=defaultdict(int)
    for stream in streams:
        count_dic[stream[0]]+=stream[1]
    count_dic=dict(sorted(count_dic.items(), key=lambda item: item[1], reverse=True))
    answer=[]
    for key in count_dic.keys():
        count=0
        for stream in streams:
            if count >= 2:
                continue
            if key==stream[0]:
                answer.append(stream[2])
                count+=1
    return answer
g1, p1=["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]

print(solution(g1, p1))
