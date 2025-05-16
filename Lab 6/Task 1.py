import sys
sys.setrecursionlimit(10**6)
m,n=map(int,input().split())
adj_list=[[] for i in range(m+1)]
color=[0]*(m+1)
for i in range(n):
    u,v=map(int,input().split())
    adj_list[u].append(v)
lst=[]
def dfs(g,u):
    global lst
    color[u]=1
    for i in g[u]:
        if color[i]==1:
            return True
        elif color[i]==0:
            x=dfs(g,i)
            if x:
                return x
    color[u]=2
    lst.append(u)
    return False

for i in range(m):
    if color[i+1]==0:
        y=dfs(adj_list,i+1)
        if y:
            print(-1)
            break
if not y:
    for i in range(len(lst)-1,-1,-1):
        print(lst[i],end=' ')