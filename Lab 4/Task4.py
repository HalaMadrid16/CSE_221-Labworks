v,e=map(int,input().split())
u=list(map(int,input().split()))
n=list(map(int,input().split()))
adj_list={i:[] for i in range(1,v+1)}
for i in range(len(u)):
    adj_list[u[i]].append(n[i])
    adj_list[n[i]].append(u[i])
odd_count=0
for i in range(len(adj_list)):
    count=len(adj_list[i+1])    
    if count%2!=0:
        odd_count+=1
if odd_count==0:
    print("Yes")
elif odd_count==2:
    print("Yes")
else:
    print("No")