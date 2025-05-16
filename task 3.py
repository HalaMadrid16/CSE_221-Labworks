var=input().split()
n=int(var[1])
lst=list(map(int,input().split()))
l,curr,best=-1,0,0
for i in range(int(var[0])):
    curr+=lst[i]
    while curr>n:
        l+=1
        curr-=lst[l]
    best=max(best,i-l)
print(best)