var=int(input())
for i in range(var):
    n=input()
    j=0
    k=len(n)-1
    while j<=k:
        flag=False
        mid_idx=(k+j)//2
        mid_val=int(n[(k+j)//2])
        if mid_val==0:
            j=mid_idx+1
        if mid_val==1:
            if mid_idx==0 or n[mid_idx-1]=='0':
                print(int(mid_idx)+1)
                flag=True
                break
            else:
                k=mid_idx-1
    if flag==False:
        print(-1)        
    