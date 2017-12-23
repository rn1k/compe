# -*- coding: utf-8 -*-

# p.48 fence repair

global n, l
n = 3
l = [8, 5, 8]

def main():
    global n
    sl = sorted(l)
    c = 0

    while (n > 1):
        t = sl[0] + sl[1]
        c += t
        sl = sl[1:]
        sl[0] = t
        n -= 1
    print(c)

if __name__ == '__main__':
    main()
