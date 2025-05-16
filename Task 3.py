v,e,s,d=map(int,input().split())
adj_list=[[] for i in range(v)]
if e==0:
    print(0)
    print(1)
else:
    color=[0]*v
    parent=[None]*v
    u=list(map(int,input().split()))
    w=list(map(int,input().split()))
    for i in range(e):
        adj_list[u[i]-1].append(w[i]-1)
        adj_list[w[i]-1].append(u[i]-1)
    for i in range(v):
        adj_list[i].sort()

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
                if y==d-1:
                    break
    if parent[d-1]==None:
        print(-1)
    else:
        lst=[]
        p=parent[d-1]
        lst.append(d-1)
        while p!=(s-1):
            lst.append(p)
            p=parent[p]
        lst.append(p)
        print(len(lst)-1)
        for i in range(len(lst)-1,-1,-1):
            print(lst[i]+1,end=' ')

