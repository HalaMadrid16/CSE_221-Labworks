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
    for j in range(len(name)-i-1):
        if name[j]>name[j+1]:
            name[j],name[j+1]=name[j+1],name[j]
            time[j],time[j+1]=time[j+1],time[j]
            location[j],location[j+1]=location[j+1],location[j]
        elif name[j]==name[j+1]:
            x,y=time[j].split(':'),time[j+1].split(':')
            x1=int(x[0])*60+int(x[1])
            y1=int(y[0])*60+int(y[1])
            if x1<y1:
                name[j],name[j+1]=name[j+1],name[j]
                time[j],time[j+1]=time[j+1],time[j]
                location[j],location[j+1]=location[j+1],location[j]
        
for i in range(len(name)):
    print(f'{name[i]} will departure for {location[i]} at {time[i]}')