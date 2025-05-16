import heapq
v,e,s,d=map(int,input().split())
weight=list(map(int,input().split()))
adj_list=[[] for i in range(v+1)]
for i in range(e):
    x,y=map(int,input().split())
    adj_list[x].append(y)
dis=[float('inf')]*(v+1)
heap=[(weight[s-1],s)]
visited=[False]*(v+1)
dis[s]=weight[s-1]
while len(heap)>0:
    curr_w,node=heapq.heappop(heap)
    if not visited[node]:
        visited[node]=True
        for n in adj_list[node]:
            if not visited[n]:
                if curr_w+weight[n-1]<dis[n]:
                    dis[n]=curr_w+weight[n-1]
                    heapq.heappush(heap,(dis[n],n))
if dis[d]==float('inf'):
    print(-1)
else:
    print(dis[d])

