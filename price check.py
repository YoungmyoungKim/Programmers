def prison(n, m, h, v):
    # Write your code here
    h.sort()
    v.sort()
    Y=[]
    leng=1
    if len(h)>1:
        for i, val in enumerate(h[1:], start=0):
            if val==h[i]+1:
                leng+=1
                Y.append(leng+1)
            else:
                leng=1
                Y.append(leng+1)
    else:
        Y.append(leng+1)

    Ymax=max(Y)
    X=[]
    leng=1
    if len(v)>1:
        for i, val in enumerate(v[1:], start=0):
            if val==v[i]+1:
                leng+=1
                X.append(leng+1)
            else:
                leng=1
                X.append(leng+1)
    else:
        X.append(leng+1)

    Xmax=max(X)
    return Xmax*Ymax

print(prison(3, 2, [1, 2, 3], [1, 2]))
#print(prison(3, 3, [2], [2]))

def closestStraightCity(c, x, y, q):
    # Write your code here
    dic={}
    for i, city in enumerate(c):
        dic[city]=(x[i], y[i])
    li=[]
    for city in c:
        temp=[]
        for x in c:
            if city==x:
               temp.append(max(max(x), max(y)))
            else:
                 distance=abs(dic[city][0]-dic[x][0])+abs(dic[city][1]-dic[x][1])
                 temp.append(distance)
        li.append(temp)
        print(li)
    return li
