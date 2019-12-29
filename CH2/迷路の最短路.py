#幅優先探索
n = 10
m = 10
field = [['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
        ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
        ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
        ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
        ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
        ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#']]
INF = 10**10

for i in range(n):
    for j in range(m):
        if field[i][j] == "S":
            sx = i
            sy = j
        if field[i][j] == "G":
            gx = i
            gy = j

d = [[0]*n for i in range(m)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    queue = []
    for i in range(n):
        for j in range(m):
            d[i][j] = INF
    d[sx][sy] = 0
    queue.append([sx,sy])

    while len(queue) != 0:
        value = queue[0]
        queue.pop(0)

        if value[0] == gx and value[1] == gy:
            break

        for i in range(4):
            nx = value[0] + dx[i]
            ny = value[1] + dy[i]

            if 0<=nx and nx<=n-1 and 0<=ny and ny<=m-1:
                if field[nx][ny] != "#" and d[nx][ny] == INF:
                    queue.append([nx,ny])
                    d[nx][ny] = d[value[0]][value[1]] + 1
    return d[gx][gy]

ans = bfs()
print(ans)
