import heapq

N,M,S,D=map(int,input().split())
adj_list=[[]for i in range(N+1)]
for i in range(M):
    u,v,w=map(int,input().split())
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))

dist1=[float('inf')]*(N+1)
dist2=[float('inf')]*(N+1)
dist1[S]=0
heap=[]
heapq.heappush(heap,(0,S))

while heap:
    d,u=heapq.heappop(heap)
    if d>dist2[u]:
        continue
    for v,weight in adj_list[u]:
        if d+weight<dist1[v]:
            dist2[v]=dist1[v]
            dist1[v]=d+weight
            heapq.heappush(heap,(dist1[v],v))
        elif dist1[v]<d+weight<dist2[v]:
            dist2[v]=d+weight
            heapq.heappush(heap,(dist2[v],v))

if dist2[D]!=float('inf') and dist2[D]>dist1[D]:
    print(dist2[D])
else:
    print(-1)