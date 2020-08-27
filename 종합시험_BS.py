def Solution(w, x):
    low=0
    high=len(w)-1

    while high>=low:
        mid=(low+high)//2

        if w[mid]>=x:
            high=mid-1
        elif w[mid]==x:
            return mid
        else:
            low=mid+1
    #answer=min(abs(W[high]-x), abs(W[low]-x))
    answer= high if abs(W[high]-x)<=abs(W[low]-x) else low
    return answer

def Solution(w, x):
    low=0
    high=len(W)-1
    #w=list(map(lambda val:val-x, w))
    while high>=low:
        mid=(low+high)//2

        if w[mid]-x>0:
            high=mid-1
        elif w[mid]-x==0:
            return mid
        else:
            low=mid+1

    return high if abs(W[high]-x)<=abs(W[low]-x) else low


W=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x=31

print(Solution(W, x))
