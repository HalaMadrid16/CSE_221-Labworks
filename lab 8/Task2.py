v,e=map(int,input().split())
adj_list=[[] for _ in range(v+1)]
for _ in range(e):
    x,y,w=map(int,input().split())
    adj_list[x].append((y,w))
edges=[]
for i in range(1,v+1):
    for  j,k in adj_list[i]:
        edges.append((i,j,k))
edges.sort(key=lambda x: x[2])
parent=[0]*(v+1)
size=[1]*(v+1)
for i in range(1,v+1):
    parent[i]=i
def find(x):
    while x==parent[x]:
        return x
    parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return False
    if size[x]<size[y]:
        x,y=y,x
    parent[y]=x
    size[x]+=size[y]
    return True
cost=0
count=0
for x,y,w in edges:
    if count==v-1:
        break
    if union(x,y):
        cost+=w
        count+=1
print(cost)