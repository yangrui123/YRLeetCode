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
    start, end = 0,1
    i, j = 0,1
    while j<n:
        if s[i]==s[j]:
            p[i][j]=1
            max_len=2
            start, end = i, j+1
        i+=1;j+=1
    for sep in range(2,n):
        for row in range(n-sep):
            col = row+sep
            if s[row]==s[col] and p[row+1][col-1]==1:
                p[row][col] = 1
                tlen = col - row + 1
                if tlen > max_len:
                    max_len = tlen
                    start, end = row, col+1
    return s[start:end]

def longestPalindrome2(s):
    n = len(s)
    if n == 0 or n == 1:
        return s
    maxLen = 1
    start = 0
    for i in xrange(n):
        if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
            start = i - maxLen - 1
            maxLen += 2
            continue

        if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
            start = i - maxLen
            maxLen += 1
    return s[start:start + maxLen]



if __name__ == '__main__':
    s="ranynarcivilwartestingwhetherthatnaptionotionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    begin = time.time()
    res = longestPalindrome2(s)
    print time.time()-begin
    print res
