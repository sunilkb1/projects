"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



"""


import itertools
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = dict(zip(nums,range(len(nums))))
        print(h_map)
        for i in range(1, len(nums)):
                comb_list = list(itertools.combinations(nums,i))
                for j in comb_list:
                    if sum(j) == target:
                        x = list(map(lambda y: h_map[y], j))
                        return(x)
                        
                        


nums=[1,3,4,5,6,9]
target=13
s=Solution()
print(s.twoSum(nums, target))