n=int(input())
adj_mat=[[0]*n for i in range(n)]
for i in range(n):
    u=list(map(int,input().split()))
    for j in range(1,len(u)):
        adj_mat[i][u[j]]=1
for i in range(n):
    for j in range(n):
        print(adj_mat[i][j],end=' ')
    print()

