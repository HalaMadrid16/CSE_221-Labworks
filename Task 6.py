import heapq
n=int(input())
lst=[]
for i in range(n):
    s=input()
    lst.append(s)
in_degree={}
for w in lst:
    for c in w:
        if c not in in_degree:
            in_degree[c]=0
adj_list={i:[] for i in in_degree.keys()}
valid=True
for i in range(len(lst)-1):
    flag=False
    for j in range(min(len(lst[i]), len(lst[i+1]))):
            if lst[i][j]!=lst[i+1][j]:
                if lst[i+1][j] not in adj_list[lst[i][j]]:
                    adj_list[(lst[i][j])].append(lst[i+1][j])
                    in_degree[lst[i+1][j]]+=1
                flag=True
                break
    if not flag and len(lst[i])>len(lst[i+1]):
       valid=False
       break
   
if not valid:
    print(-1)
else:
    q=[]
    for i in in_degree.keys():
        if in_degree[i]==0:
            heapq.heappush(q,i)
    ans=''
    while len(q)>0:
        x=heapq.heappop(q)
        ans+=x
        for i in sorted(adj_list[x]):
            in_degree[i]-=1
            if in_degree[i]==0:
                heapq.heappush(q,i)
    if len(ans)!=len(in_degree):
        print(-1)
    else:
        print(ans)
