# -*- coding: utf-8 -*-

# p.34 和をちょうどkにできるか判定

global n, a, k

# data1
n = 4
a = [1, 2, 4, 7]
k = 13

# # data 2
# n = 4
# a = [1, 2, 4, 7]
# k = 15

# depth-first search
def dfs(i, psum):
    print(i, psum)
    if (i == n): # 全部足した場合にkにとなるか
        return (psum == k)
    elif (dfs(i+1, psum)): # a[i] を使わない場合
        return True
    elif (dfs(i+1, psum + a[i])): # a[i] を使う場合
        return True
    else:
        return False

def main():
    if (dfs(0, 0)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
