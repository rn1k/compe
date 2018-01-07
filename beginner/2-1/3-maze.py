# -*- coding: utf-8 -*-

# p.37 迷路

from collections import deque

global n, m, maze
n = 10
m = 10
maze_str="""
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#
"""
maze = list(map(list, maze_str.split("\n")[1:-1]))

global sx, sy, gx, gy, dx, dy
sx, sy = 0, 1
gx, gy = 9, 8
dx = [ 1, 0, -1, 0 ]
dy = [ 0, 1, 0, -1 ]

# breadth-first search
def bfs():
    INF = 10000000
    d = [[INF for j in range(m)] for i in range(n)]

    start = (sx, sy)
    goal = (gx, gy)

    q = deque([])
    q.append(start)
    d[sx][sy] = 0

    while (len(q)):
        p = q.popleft()
        if ( p == goal ):
            break
        # 4方向
        for i in range(4):
            x, y = p
            nx = x + dx[i]
            ny = y + dy[i]
            if ( 0<=nx<n and 0<=ny<m and maze[nx][ny]!="#" and d[nx][ny]==INF ):
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1
    return d[gx][gy]

def main():
    print(bfs())

if __name__ == '__main__':
    main()
