#! /usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    int_max = 2**31
    new_intgr = 0
    flag = 1
    if x < 0:
        x = -x
        flag = -1
    l = len(str(x))
    for i in range(l):
        x, mod = divmod(x, 10)
        new_intgr += mod * (10 ** (l - i - 1))
    if new_intgr > int_max:
        return 0
    return new_intgr * flag

def another(x):
    s = cmp(x, 0)
    r = int(`s * x`[::-1])
    return s * r * (r < 2 ** 31)

if __name__ == '__main__':
    x = 1534236469
    res = reverse(x)
    print res