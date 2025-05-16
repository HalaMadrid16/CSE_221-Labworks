def fastmod(a,b,m):
    if b==1:
        return a%m
    if b%2==0:
        div=fastmod(a,b//2,m)
        return (div)**2%m
    else:
        div=fastmod(a,b-1,m)
        return (div*a)%m
def geometricsum(a,b,m):
    if b==1:
        return a%m
    if b%2==0:
        sum=geometricsum(a,b//2,m)
        return (sum+fastmod(a,b//2,m)*sum)%m
    else:
        sum=geometricsum(a,b-1,m)
        return (sum+fastmod(a,b,m))%m
var=int(input())
for i in range(var):
    a,b,m=map(int,input().split())
    print(geometricsum(a,b,m))
