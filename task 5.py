import sys
sys.setrecursionlimit(10**6)
v,e=map(int,input().split())
adj_list=[[] for i in range(v)]
for i in range(e):
    u,n=map(int,input().split())
    adj_list[u-1].append(n-1)
color=[0]*v
flag=False
def dfs(g,u):
    global flag
    color[u]=1
    for i in g[u]:
        if color[i]==1:
            flag=True
            return 
        elif color[i]==0:
           dfs(g,i)
           if flag:
               return
    color[u]=2
   
for i in range(v):
    if color[i]==0:
        dfs(adj_list,i)
        if flag:
            print('YES')
            break
if not flag:
    print('NO')