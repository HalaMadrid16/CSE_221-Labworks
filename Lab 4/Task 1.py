n,m=list(map(int,input().split()))
matrix=[[0]*n for i in range(n)]
for i in range(m):
    u,v,w=list(map(int,input().split()))
    matrix[u-1][v-1]=w
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=' ')
    print()
