#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


def searchInsert( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ll, lr = 0, len(nums) - 1
    while ll <= lr:
        mid = ll + lr >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            lr = mid - 1
        else:
            ll = mid + 1
    return lr + 1


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 0
    idx = searchInsert(nums, target)
    print idx