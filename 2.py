x=int(input())
name=[]
time=[]
location=[]
for i in range(x):
    y=input().split()
    name.append(y[0])
    time.append((y[len(y)-1]))
    location.append(y[len(y)-3])
for i in range(len(name)-1):
    max_index=i
    for j in range(i+1,len(name)):
        if name[j]<name[max_index]:
            max_index=j
        elif name[j]==name[max_index]:
            x,y=time[j].split(':'),time[max_index].split(':')
            x1=int(x[0])*60+int(x[1])
            y1=int(y[0])*60+int(y[1])
            if x1>y1:
                max_index=j
            elif x1==y1:
                if max_index>j:
                    max_index=j
    if max_index!=i:
        name[i],name[max_index]=name[max_index],name[i]
        time[i],time[max_index]=time[max_index],time[i]
        location[i],location[max_index]=location[max_index],location[i]
for i in range(len(name)):
    print(f'{name[i]} will departure for {location[i]} at {time[i]}')