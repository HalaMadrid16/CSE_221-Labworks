var=input().split()
s=int(var[1])
lst=input().split()
i=0
j=len(lst)-1
flag=0
while i<j:
    if int(lst[i])+int(lst[j])==s:
        print(f'{i+1} {j+1}')
        flag=1
        break
    elif int(lst[i])+int(lst[j])>s:
        j-=1
    else:
        i+=1
if flag==0:
    print('No pair found')