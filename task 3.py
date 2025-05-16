var=list(map(int,input().split()))
a=var[0]
b=var[1]
def fastmod(a,b):
    if b==1:
        return a%107
    if b%2==0:
        div=fastmod(a,b//2)
        return (div)**2%107
    else:
        div=fastmod(a,b-1)
        return (div*a)%107
print(fastmod(a,b))