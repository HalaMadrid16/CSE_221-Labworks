var=int(input())
arr=list(map(int,input().split()))
def sort(arr):
    if len(arr)==1:
        return arr
    else:
        mid=len(arr)//2
        left=sort(arr[:mid])
        right=sort(arr[mid:])
        if type(left[0])==int:
            left=[left,0]
        if type(right[0])==int:
            right=[right,0]
        curr= merge(left[0],right[0])
        return (curr[0],curr[1]+left[1]+right[1])
def merge(left,right):
    inv=0
    i,j=0,0
    lst=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            lst.append(left[i])
            i+=1
        else:
            inv+=len(left)-i
            lst.append(right[j])
            j+=1
    while i<len(left):
        lst.append(left[i])
        i+=1
    while j<len(right):
        lst.append(right[j])
        j+=1
    return [lst,inv]
res=sort(arr)
print(res[1])
for i in range(len(res[0])):
    print(res[0][i],end=' ')