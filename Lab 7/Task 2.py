import heapq
v,e,s_a,s_b=list(map(int,input().split()))
adj_list=[[] for i in range(v+1)]
for i in range(e):
    x,y,w=map(int,input().split())
    adj_list[x].append((y,w))
def dijkstra(v,s,adj_list):
    parent=[None]*(v+1)
    dis=[float('inf')]*(v+1)
    visited=[False]*(v+1)
    dis[s]=0
    heap=[(0,s)]
    while len(heap)>0:
        curr_dis,node=heapq.heappop(heap)
        if not visited[node]:
            visited[node]=True
            for n,w in adj_list[node]:
                if not visited[n]:
                    distance=curr_dis+w
                    if distance<dis[n]:
                        dis[n]=distance
                        parent[n]=node
                        heapq.heappush(heap,(dis[n],n))
    return dis
if s_a==s_b:
    print(0,s_a)
else:
    dis_a=dijkstra(v,s_a,adj_list)
    dis_b=dijkstra(v,s_b,adj_list)
    max_dis,node=float('inf'),float('inf')
    for i in range(len(dis_a)):
        if dis_a[i]!=float('inf') and dis_b[i]!=float('inf'):
            curr_max=max(dis_a[i],dis_b[i])
            if curr_max<max_dis:
                max_dis,node=curr_max,i
    if max_dis==float('inf') and node==float('inf'):
        print(-1)
    else:
        print(max_dis,node)