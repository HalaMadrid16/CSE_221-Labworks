from collections import deque
n=int(input())
x_i,y_i,x_f,y_f=map(int,input().split())
x_i-=1
x_f-=1
y_i-=1
y_f-=1
visit=[[-1]*n for i in range(n)]
moves=[
        (2, 1), (1, 2),
        (-1, 2), (-2, 1),
        (-2, -1), (-1, -2),
        (1, -2), (2, -1) ]
q=deque()
def bfs():
    while len(q)>0:
        v=q.popleft()
        if v==(x_f,y_f):
            return visit[v[0]][v[1]]
        for dx,dy in moves:
            new_x=v[0]+dx
            new_y=v[1]+dy
            if 0<=new_x<n and 0<=new_y<n:
                pos=(new_x,new_y)
                if visit[new_x][new_y]==-1:
                    visit[new_x][new_y]=visit[v[0]][v[1]] +1
                    q.append(pos)
    return -1
q.append((x_i,y_i))
visit[x_i][y_i]=0
res=bfs()
print(res)
