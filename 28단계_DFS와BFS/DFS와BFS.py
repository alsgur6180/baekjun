n,m,v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    graph[x][y] =1
def dfs(x,y):
    if x<=0 or x>=n or y<=0 or y>=n:
        return 0
    if graph[x][y] ==1:
        graph[x][y] =0
        print(y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        
    return 0
print(v)
dfs(v,graph[v].index(1))
