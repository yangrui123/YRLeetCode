#! /usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import time


def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return r


if __name__ == '__main__':
    S = [-15,6,7,0,-14,-5,-3,-10,-14,1,-14,-1,-11,-11,-15,-1,3,-12,7,14,1,6,-6,7,1,1,0,-4,8,7,2,1,-2,-6,-14,-9,-3,-1,-12,-2,7,11,4,12,-14,-4,-4,4,-1,10,3,-14,1,12,0,10,-9,8,-9,14,-8,8,0,-3,10,-6,4,-8,0,-1,-3,-8,-4,8,11,-3,-11,-8,8,3,10,-3,-4,-4,-14,12,13,-8,-3,12,-8,4,5,-1,-14,-8,8,-3,-9,-15,12,-5,-7,-15,-12,11,-11,14,11,12,3,6,-6]
    #S = [-1, 0, 1, 2, -1, -4]
    begin = time.time()
    record_list = threeSum(S)
    print(time.time()-begin)
    print(record_list)
