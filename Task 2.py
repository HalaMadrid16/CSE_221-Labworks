n,m=list(map(int,input().split()))
adjacency_list={i:[] for i in range(1,n+1)}
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
for i in range(m):
    adjacency_list[u[i]].append((v[i],w[i]))
for i in range(len(adjacency_list)):
            print(i+1, end=': ')
            for j in range(len(adjacency_list[i+1])):
                print(adjacency_list[i+1][j], end=' ')
            print() 