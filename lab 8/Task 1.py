v,c=map(int,input().split())
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
        return size[x]
    if size[x]<size[y]:
        x,y=y,x
    parent[y]=x
    size[x]+=size[y]
    return size[x]
for i in range(c):
    a,b=map(int,input().split())
    print(union(a,b))
    