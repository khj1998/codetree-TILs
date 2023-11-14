from collections import deque

n,m = map(int,input().split())
q = deque()
dx,dy = [-1,1,0,0],[0,0,-1,1]
array = []
check = [[False]*m for _ in range(n)]

for _ in range(n):
    array.append(list(map(int,input().split())))


for i in range(n):
    for j in range(m):
        if array[i][j] == 2:
            q.append((i,j))
            array[i][j] = 0
            check[i][j] = True
            break

while q:
    x,y = q.popleft()

    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]

        if 0<=px<n and 0<=py<m and not check[px][py] and array[px][py]==1:
            check[px][py] = True
            array[px][py] = array[x][y] + 1
            q.append((px,py))

for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            print(0,end=" ")
        elif not check[i][j]:
            print(-1,end=" ")
        else:
            print(array[i][j],end=" ")
    print()