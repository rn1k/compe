# -*- coding: utf-8 -*-

# p.43 区間スケジューリング

global n, s, t
n = 5
s = [ 1, 2, 4, 6, 8 ]
t = [ 3, 5, 7, 9, 10 ]

def main():
    count = 0
    last_end = 0
    for start, end in sorted(zip(s, t), key=lambda tpl: tpl[1]):
        if (last_end < start):
            count += 1
            last_end = end
    print(count)

if __name__ == '__main__':
    main()
