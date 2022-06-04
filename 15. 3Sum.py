# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, val in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            l, r = i+1, len(nums)-1
            while l<r:
                threesum = nums[i]+nums[l]+nums[r]
                if threesum<0:
                    l+=1
                elif threesum>0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

# neetcode