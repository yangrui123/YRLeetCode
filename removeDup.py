#! /usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    count = 1
    i = 0;j = 1
    length = len(nums)
    while(True):
        if nums[i] != nums[j]:
            count += 1
            nums[i+1] = nums[j]
            if j+1 >=length:
                return count
            i += 1; j+=1
        else:
            if j+1 >= length:
                return count
            nums[i+1] = nums[j+1]
            j+=1



if __name__ == '__main__':
    nums = [1,2,2,3,4,4,4,4,5,5,6,6]
    count = removeDuplicates(nums)
    print(count)
    print(nums[:count])
