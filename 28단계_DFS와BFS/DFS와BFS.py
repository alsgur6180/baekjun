n,m,v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    graph[x][y] =1
    graph[y][x] =1
def dfs(start,visited):
    visited += [start]
    for c in range(len(graph[start])):
        if graph[start][c] == 1 and(c not in visited):
            dfs(c,visited)
    return visited
print(dfs(v,[]))

