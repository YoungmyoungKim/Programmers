def solution(n, computers):
    stack=[]
    count=1
    graph={i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 and i!=j:
                graph[i].append(j)
    paths=map(sorted, [dfs(graph, node) for node in graph])

    return len(set([''.join(map(str, path)) for path in paths]))

def dfs(graph, start):
    visited=[]
    stack=[start]

    while stack:
        v=stack.pop()
        if v not in visited:
            visited.append(v)
            stack.extend([x for x in graph[v] if x not in visited])
    return visited
