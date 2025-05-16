len1=int(input())
lst1=input().split()
len2=int(input())
lst2=input().split()
i,j=0,0
s=''
while i<len1 and j<len2:
    if int(lst1[i])<int(lst2[j]):
        s+=lst1[i]+' '
        i+=1
    else:
        s+=lst2[j]+' '
        j+=1
while i<len1:
    s+=lst1[i]+' '
    i+=1
while j<len2:
    s+=lst2[j]+' '
    j+=1
print(s)    
