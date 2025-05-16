def bfs(s,f):
    q=[]
    q.append(s-1)
    color[s-1]=1
    while len(q)>0:
        x=q.pop(0)
        for y in adj_list[x]:
            if color[y]==0:
                color[y]=1
                parent[y]=x
                q.append(y)
                if y==f-1:
                    break
def path(d,lst):
    p=parent[d-1]
    lst.append(d-1)
    while p!=(s-1):
        lst.append(p)
        p=parent[p]
    lst.append(p)
v,e,s,k,d=map(int,input().split())
adj_list=[[] for i in range(v)]
for i in range(e):
    u,n=map(int,input().split())
    adj_list[u-1].append(n-1)
color=[0]*v
parent=[None]*v
for i in range(v):
        adj_list[i].sort()
bfs(s,k)
bfs(k,d)
if parent[k-1]==None and parent[d-1]==None:
     print(-1)
else:
     lst=[]
     path(k,lst)
     path(d,lst)
print(len(lst)-1)
for i in range(len(lst)-1,-1,-1):
    print(lst[i]+1,end=' ')