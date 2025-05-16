v,e=map(int,input().split())
adj_list={i:[] for i in range(1,v+1)}
u=list(map(int,input().split()))
w=list(map(int,input().split()))
for i in range(e):
    adj_list[u[i]].append(w[i])
in_list=[0]*v
out_list=[0]*v
for i in range(1,v+1):
    in_list[i-1]=len(adj_list[i])
    for j in range(len(adj_list[i])):
        out_list[adj_list[i][j]-1]+=1
for i in range(v):
    print(-in_list[i]+out_list[i],end=' ')