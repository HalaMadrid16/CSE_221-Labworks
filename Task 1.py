v,e=map(int,input().split())
adj_list=[[] for i in range(v)]
color=[0]*v
for i in range(e):
    u,v=map(int,input().split())
    adj_list[u-1].append(v)
    adj_list[v-1].append(u)
q=[]
q.append(0)
color[0]=1
print(1,end=' ')
while len(q)>0:
    u=q.pop(0)
    for v in range(len(adj_list[u])):
        if color[adj_list[u][v]-1]==0:
            color[adj_list[u][v]-1]=1
            print(adj_list[u][v],end=' ')
            q.append(adj_list[u][v]-1)

