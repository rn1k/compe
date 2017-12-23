# -*- coding: utf-8 -*-

# p.47 saruman

global n, r, xl

n = 6
r = 10
xl = [1, 7, 15, 20, 30, 50]

def main():
    global xl

    i = 0
    c = 0
    while (i < n):
        s = xl[i]
        while (i<n and xl[i] <= s+r):
            i += 1
        p = xl[i-1]

        while (i<n and xl[i] <= p+r):
            i += 1
        c += 1
    print(c)

if __name__ == '__main__':
    main()
