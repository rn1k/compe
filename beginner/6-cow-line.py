# -*- coding: utf-8 -*-

# p.45 辞書順

global n, s

n = 6
s = "ACDBCB"

def main():
    global s

    while (len(s) > 1):
        # i番目が同じ文字だった場合、i+1番目の辞書順を調べる
        for i in range(n):
            if ( s[i] < s[-(i+1)]): # 先頭のが早い
                print(s[0], end="")
                s = s[1:]
                break
            elif ( s[i] > s[-(i+1)]): # 末尾のが早い
                print(s[-1], end="")
                s = s[:-1]
                break
    # 最後の1文字
    print(s)

if __name__ == '__main__':
    main()
