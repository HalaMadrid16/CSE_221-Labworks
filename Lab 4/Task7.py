import math
n,q=map(int,input().split())
adj_list=[[] for i in range(n)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j and math.gcd(i,j)==1:
            adj_list[i-1].append(j)
for i in range(q):
    u,v=list(map(int,input().split()))
    if v<=len(adj_list[u-1]):
        print(adj_list[u-1][v-1])
    else:
        print(-1)