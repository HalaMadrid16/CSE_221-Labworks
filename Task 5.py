from collections import deque
v=int(input())
adj_list=[[] for i in range(v+1)]
for i in range(v-1):
    u,w=map(int,input().split())
    adj_list[u].append(w)
    adj_list[w].append(u)

def bfs(n):
    q = deque()
    max_level=0
    q.append((n,0))
    deep=n
    color=[0]*(v+1)
    color[n]=1
    while len(q)>0:
        x, l = q.popleft()
        if l>max_level:
            max_level=l
            deep=x
        for i in adj_list[x]:
            if color[i]==0:
                color[i]=1
                q.append((i,l+1))
    return deep,max_level
deep1,_=bfs(1)
deep2,l=bfs(deep1)
print(l)
print(deep1,deep2)
        
