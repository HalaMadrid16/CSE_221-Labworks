var=int(input())
arr=list(map(int,input().split()))
def pairmax(arr):
    if len(arr)==1:
        return arr[0]
    else:
        mid=len(arr)//2
        left=pairmax(arr[:mid])
        right=pairmax(arr[mid:])
        mer=merge(arr[:mid],arr[mid:])
        return max(left,right,mer)
def merge(left,right):
    max1=max(left)
    max2=max(right)
    min2=min(right)
    if abs(min2)>max2:
        max2=min2
    return max1+(max2**2)
print(pairmax(arr))