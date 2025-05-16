v,e=map(int,input().split())
adj_list=[[] for i in range(v+1)]
for i in range(e):
    u,w=map(int,input().split())
    adj_list[u].append(w)
    adj_list[w].append(u)
color=[-1]*(v+1)
q=[]
total=0
for i in range(1,v+1):
    if color[i]==-1:
        q.append(i)
        color[i]=0
        c0,c1=1,0
        while len(q)>0:
            x=q.pop(0)
            curr_color=color[x]
            for i in adj_list[x]:
                if color[i]==-1:
                    color[i]=1-curr_color
                    if color[i]==0:
                        c0+=1
                    else:
                        c1+=1
                    q.append(i)
        total+=max(c0,c1)
print(total)
