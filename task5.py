var=input().split()
n=int(var[1])
lst=list(map(int,input().split()))
for i in range(n):
    pair=list(map(int,input().split()))
    min=pair[0]
    max=pair[1]
    right=0
    left=len(lst)-1
    while lst[right]<min and lst[left]>max:
        right+=1
        left-=1
    while lst[left]>max:
        left-=1
    while lst[right]<min:
        right+=1
    print(left-right+1)

