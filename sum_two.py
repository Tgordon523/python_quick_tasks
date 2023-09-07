#!/usr/bin/env python
### Add Two
def sum_two_index(nums:list, result:int):
    ### Return two indexes for the proper sums
    prevMat = {}

    for i, v in enumerate(nums):
        # print(v)
        diff = result - v 
        if diff in prevMat:
            return [prevMat[diff], i]
        prevMat[v] = i
    return      
