# -*- coding: utf-8 -*-

# p.56 LCS(longest common subsequence)

global n, m, s, t
n = 4
m = 4
s = "abcd"
t = "becd"

global dp
dp = [[0 for j in range(m+1)] for i in range(n+1)]

def main():
    for i in range(n):
        for j in range(m):
            if (s[i] == t[j]):
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    print(dp)
    print(dp[n][m])


if __name__ == '__main__':
    main()
