#! /usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # odd number: the median index is n-1/2
    # even number: the median index is n-1/2,n/2
    m = len(nums1);n = len(nums2)
    if m==0:
        if n%2==0:
            return nums2[n-1>>1]+nums2[n>>1]>>1
        else:
            return nums2[n-1>>1]
    elif n==0:
        if m%2==0:
            return nums1[m-1>>1]+nums1[m>>1]>>1
        else:
            return nums1[m-1>>1]
    elif m==1 and n==1:
        return nums1[0]+nums2[0]>>1
    nums = (m+n>>1)+1
    ml=0;mr=m-1;nl=0;nr=n-1
    count = 0
    while(True):
        if mr-ml==1 and nr-nl==1:
            if nums1[mr]>nums2[nr]:
                return nums1[ml]
            elif nums2[nr]>nums1[mr]:
                return nums2[nl]
        elif mr-ml==1 and nr-nl==0:
            if nums1[mr]>nums2[nr]:
                return max(nums1[ml],nums2[nr])
            else:
                return max(nums1[mr],nums2[nr])
        elif mr-ml==0 and nr-nl==1:
            if nums2[nr]>nums1[mr]:
                return max(nums2[nl],nums1[mr])
            else:
                return max(nums2[nr],nums1[mr])
        mm = (ml+mr)>>1;mn = (nl+nr)>>1
        if nums1[mm]>nums2[mn]:
            if count+mn-nl >=nums:
                return nums2[nl+nums-count-1]
            count += mn-nl
            mr = mm;nl=mn
        else:
            if count+mm-ml >=nums:
                return nums1[ml+nums-count-1]
            count += mm-ml
            ml = mm;nr=mn


if __name__ == '__main__':
    nums1 = [1, 2,3,4,5,6,7,8,9,10]
    nums2 = [11]
    res = findMedianSortedArrays(nums1,nums2)
    print(res)