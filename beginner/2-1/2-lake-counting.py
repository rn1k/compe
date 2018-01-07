# -*- coding: utf-8 -*-

# p.35 水たまりカウント

global n, m, field

# data1
n = 10
m = 12
field_str = """
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
"""
field = list(map(list, field_str.split("\n")[1: -1]))
# print(field)

# depth-first search
def dfs(x, y):
    field[x][y] = "."
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx = x + dx
            ny = y + dy
            if ( 0 <= nx < n and 0 <= ny < m and field[nx][ny] == "W"):
                dfs(nx, ny)

def main():
    count = 0
    for i in range(n):
        for j in range(m):
            if ( field[i][j]=="W"):
                # (i,j) に隣接するものを消していく
                dfs(i, j)
                count += 1
    print(count)

if __name__ == '__main__':
    main()
