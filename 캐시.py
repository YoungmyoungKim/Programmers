def solution(cacheSize, cities):
    cache=[]
    Exetime=0
    for city in cities:
        city=city.lower()
        if city in cache:
            Exetime+=1
            cache.remove(city)
        else:
            if len(cache)>=cacheSize and cacheSize !=0:
                cache.pop(0)
            elif cacheSize==0:
                Exetime+=5
                continue
            Exetime+=5
        cache.append(city)

    return Exetime

ca1, city1=3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
ca2, city2=3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
ca3, city3=2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
ca4, city4=5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
ca5, city5=2, ["Jeju", "Pangyo", "NewYork", "newyork"]
ca6, city6=0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(ca1, city1))
print(solution(ca2, city2))
print(solution(ca3, city3))
print(solution(ca4, city4))
print(solution(ca5, city5))
print(solution(ca6, city6))
