import sys
sys.setrecursionlimit(2*100000+5)
v,e=map(int,input().split())
adj_list=[[] for i in range(v)]
color=[0]*v
u=list(map(int,input().split()))
n=list(map(int,input().split()))    
for i in range(len(u)):
    adj_list[u[i]-1].append(n[i]-1)
    adj_list[n[i]-1].append(u[i]-1)
def dfs(g,u):
    color[u]=1
    print(u+1,end=' ')
    for v in range(len(g[u])):
        if color[g[u][v]]==0:
            dfs(g,g[u][v])

dfs(adj_list,0)
