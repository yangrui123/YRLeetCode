#! /usr/bin/env python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys

"""
    reference:
    https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation/6
"""

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    n1 ,n2 = len(nums1),len(nums2)
    if n1>n2:
        n1, n2, nums1, nums2 = n2, n1, nums2, nums1
    lo, hi = 0, n1*2
    while(lo<=hi):
        mid1 = lo+hi>>1
        mid2 = n1+n2-mid1
        l1 = -sys.maxint if mid1==0 else nums1[mid1-1>>1]
        l2 = -sys.maxint if mid2==0 else nums2[mid2-1>>1]
        r1 = sys.maxint if mid1==n1*2 else nums1[mid1>>1]
        r2 = sys.maxint if mid2==n2*2 else nums2[mid2>>1]
        if l1>r2:
            hi = mid1 - 1
        elif l2>r1:
            lo = mid1 + 1
        else:
            return (max(l1,l2)+min(r1,r2))/2.0


if __name__ == '__main__':
    nums1 = [1,2,3,4,5,9,10,11]
    nums2 = [3,4,5,6,7,8]
    res = findMedianSortedArrays(nums1,nums2)
    print(res)