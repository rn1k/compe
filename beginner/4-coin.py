# -*- coding: utf-8 -*-

# p.42 貪欲法

global V, C, A
V = [ 1, 5, 10, 50, 100, 500 ]

# data
C = [ 3, 2, 1, 3, 0, 2 ]
A = 620

def main():
    global A
    ans = 0
    for value, n in reversed(list(zip(V, C))):
        t = min( A // value, n )
        A -= value * t
        ans += t
    print(ans)

if __name__ == '__main__':
    main()
