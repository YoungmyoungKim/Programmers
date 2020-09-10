def solution(operations):
    heap=[]
    for op in operations:
        x, val=op.split(' ')
        if x=='I':
            heap.append(int(val))
        elif len(heap) != 0 and val=='1':
            heap.remove(max(heap))
        elif len(heap) != 0 and val=='-1':
            heap.remove(min(heap))

    return [max(heap), min(heap)] if len(heap) != 0 else [0, 0]

operations1=["I 16","D 1"]
operations2=["I 7","I 5","I -5","D -1"]

print(solution(operations1))
print(solution(operations2))
