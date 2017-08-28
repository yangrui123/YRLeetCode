#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import sys

def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = len(nums)
    nums.sort()
    cur_min = sys.maxint
    cur_val = 0
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        ll, lr = i + 1, n - 1
        tgt = target - nums[i]
        while ll < lr:
            tmp = nums[ll] + nums[lr]
            if tmp == tgt:
                return target
            elif tmp < tgt:
                if tgt - tmp < cur_min:
                    cur_min = tgt - tmp
                    cur_val = tmp + nums[i]
                ll += 1
            else:
                if tmp - tgt < cur_min:
                    cur_min = tmp - tgt
                    cur_val = tmp + nums[i]
                lr -= 1
    return cur_val

if __name__ == '__main__':
    nums = [0,1,2]
    target = 3
    res = threeSumClosest(nums, target)
    print res
