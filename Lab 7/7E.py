import heapq

N,M=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))

adj_list=[[]for i in range(N+1)]
for i in range(M):
    adj_list[u[i]].append((v[i],w[i]))
    
dist=[[float('inf')]*2 for i in range(N+1)]
dist[1][0]=0
dist[1][1]=0
heap=[]
heapq.heappush(heap,(0,1,0))
heapq.heappush(heap,(0,1,1))

while heap:
    d,u,last_parity=heapq.heappop(heap)
    if u==N:
        print(d)
        exit()
    if d>dist[u][last_parity]:
        continue
    for v,weight in adj_list[u]:
        new_parity=weight%2
        if d+weight<dist[v][new_parity] and new_parity!=last_parity:
            dist[v][new_parity]=d+weight
            heapq.heappush(heap,(dist[v][new_parity],v,new_parity))

print(-1)