#!/usr/bin/env python
### Add Two

example1 = [2, 3, 5, 1]
result1 = 3
example2 = [3,2,1,4]
result2 = 5

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

print(sum_two_index(example2, result2))        
