import sys
sys.setrecursionlimit(10**6)
v,r=map(int,input().split())
adj_list=[[] for i in range(v+1)]
for i in range(v-1):
    u,w=map(int,input().split())
    adj_list[u].append(w)
    adj_list[w].append(u)
lst=[]
s=int(input())
for i in range(s):
    lst.append(int(input()))
visited=[0]*(v+1)
subtree=[0]*(v+1)
def dfs(n):
    visited[n]=1
    curr=1
    for i in adj_list[n]:
        if visited[i]==0:
            curr+=dfs(i)
    subtree[n]=curr
    return curr
dfs(r)
for i in lst:
    print(subtree[i])