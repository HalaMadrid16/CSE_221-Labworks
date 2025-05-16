def bst(arr,lst):
    if len(arr)==1:
        lst.append(arr[0])
        return lst
    if len(arr)==0:
        return lst
    mid=len(arr)//2
    lst.append(arr[mid])
    bst(arr[:mid],lst)
    bst(arr[mid+1:],lst)
    return lst
var=int(input())
arr=list(map(int,input().split()))
lst=[]
lst=bst(arr,lst)
for i in range(len(lst)):
    print(lst[i],end=' ')