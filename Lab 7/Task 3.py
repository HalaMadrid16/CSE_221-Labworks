import heapq
v,e=map(int,input().split())
adj_list=[[] for i in range(v+1)]
for i in range(e):
    x,y,w=map(int,input().split())
    adj_list[x].append((y,w))
    adj_list[y].append((x,w))
parent=[None]*(v+1)
dis=[float('inf')]*(v+1)
visited=[False]*(v+1)
dis[1]=0
heap=[(0,1)]
while len(heap)>0:
    curr_dis,node=heapq.heappop(heap)
    if not visited[node]:
        visited[node]=True
        for n,w in adj_list[node]:
            if not visited[n]:
                maximum=max(curr_dis,w)
                if maximum<dis[n]:
                    dis[n]=maximum
                    heapq.heappush(heap,(dis[n],n))
                
for i in range(1,len(dis)):
    if dis[i]==float('inf'):
        print(-1,end=' ')
    else:
        print(dis[i],end=' ')