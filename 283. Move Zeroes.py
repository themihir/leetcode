# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # # 1st approach
        # l=len(nums)
        # i=0
        # for j in range(l):
        #     if nums[j]!=0:
        #         nums[i]=nums[j]
        #         i+=1
        
        # while i<l:
        #     nums[i]=0
        #     i+=1

        # 2nd approach
        l=len(nums)
        i=0
        for j in range(l):
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
