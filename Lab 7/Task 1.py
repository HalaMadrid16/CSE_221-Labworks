import heapq
v,e,s,d=list(map(int,input().split()))
adj_list=[[] for i in range(v+1)]
parent=[None]*(v+1)
dis=[float('inf')]*(v+1)
visited=[False]*(v+1)
dis[s]=0
heap=[(0,s)]
x=list(map(int,input().split()))
y=list(map(int,input().split()))
w=list(map(int,input().split()))
for i in range(e):
    adj_list[x[i]].append((y[i],w[i]))
while len(heap)>0:
    curr_dis,node=heapq.heappop(heap)
    if node==d:
        break
    if not visited[node]:
        visited[node]=True
        for n,w in adj_list[node]:
            if not visited[n]:
                distance=curr_dis+w
                if distance<dis[n]:
                    dis[n]=distance
                    parent[n]=node
                    heapq.heappush(heap,(dis[n],n))
if dis[d] == float('inf'):
    print(-1)

else:
    print(dis[d])
    if s==d:
        print(s)
    else:
        path=[]
        path.append(d)
        p=parent[d]
        while p!=s:
            path.append(p)
            p=parent[p]
        path.append(s)
        for i in range(len(path)-1,-1,-1):
            print(path[i],end=' ')
