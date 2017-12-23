# -*- coding: utf-8 -*-

# p.52 napsack

global n, wv, W
n = 4
wv = [(2,3), (1,2), (3,4), (2,2)]
wl = [w for w, v in wv]
vl = [v for w, v in wv]
W = 5

# 深さ優先
def dfs(i, w):
    if (i == n):
        ret = 0
    elif (w < wl[i]):
        ret = dfs(i+1, w)
    else:
        ret = max(dfs(i+1, w), dfs(i+1, w-wl[i]) + vl[i])
    return ret

# dpメモ
global dp
dp = [[-1 for i in range(W+1)] for j in range(n+1)]
global dp2
dp2 = [[0 for i in range(W+1)] for j in range(n+1)]

def rec(i, w):
    print(i, w)
    if (dp[i][w] >= 0):
        return dp[i][w]
    if (i == n):
        ret = 0
    elif (w < wl[i]):
        ret = rec(i+1, w)
    else:
        ret = max(rec(i+1, w), rec(i+1, w-wl[i]) + vl[i])
    dp[i][w] = ret
    return ret

def dif():
    # n/w 0  1  2  3  4  5
    #  0  0  2  3  5  6  7
    #  1  0  2  2  4  6  6
    #  2  0  0  2  4  4  6
    #  3  0  0  2  2  2  2
    #  4  0  0  0  0  0  0
    for i in reversed(range(n)):
        for j in range(W+1):
            if (j < wl[i]):
                dp2[i][j] = dp2[i+1][j]
            else:
                dp2[i][j] = max(dp2[i+1][j], dp2[i+1][j-wl[i]]+vl[i])
    return dp2[0][W]



def main():
    print(dfs(0, W))
    print(rec(0, W))
    print(dif())
    print(dp2)


if __name__ == '__main__':
    main()
