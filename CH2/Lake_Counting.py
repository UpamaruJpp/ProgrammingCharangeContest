n = 10
m = 12
field = [['W', '.', '.',  '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
         ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
         ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
         ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
         ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
         ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
         ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
         ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.']]


def dfs(x,y):
    field[x][y] = '.'

    for dx in range(-1,2):
        for dy in range(-1,2):
            nx = x + dx
            ny = y + dy

            if 0<=nx and nx<=n-1 and 0<=ny and ny<=m-1:
                if field[nx][ny] == 'W':
                    dfs(nx,ny)
cnt = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == 'W':
            dfs(i,j)
            cnt+=1
print(cnt)