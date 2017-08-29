#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import time
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    if n == 1 or n == 0:
        return s
    p = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        p[i][i]=1
    max_len = 1
    rstr = s[0]
    i, j = 0,1
    while j<n:
        if s[i]==s[j]:
            p[i][j]=1
            max_len=2
            rstr = s[i:j+1]
        i+=1;j+=1
    for sep in range(2,n):
        for row in range(n-sep):
            col = row+sep
            if s[row]==s[col] and p[row+1][col-1]==1:
                p[row][col] = 1
                tlen = col - row + 1
                if tlen > max_len:
                    max_len = tlen
                    rstr = s[row:col + 1]
    return rstr

def longestPalindrome2(s):
    n = len(s)
    if n==0 or n==1:
        return s
    p = [[0 for col in range(n)] for row in range(n)]
    for sep in range(n):
        for row in range(n):
            col = row+sep
            if col >= n:
                break
            if s[row]==s[col]:
                if col-1>=row+1:
                    if p[row+1][col-1]==1:
                        p[row][col] = 1
                else:
                    p[row][col] = 1
    max_len = 0
    rstr = ""
    for i in range(n):
        for j in range(i,n):
            if p[i][j] == 1:
                tlen = j-i+1
                if tlen > max_len:
                    max_len = tlen
                    rstr = s[i:j+1]
    return rstr


if __name__ == '__main__':
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    #s = 'aaaa'
    begin = time.time()
    res = longestPalindrome(s)
    print time.time()-begin
    print res
