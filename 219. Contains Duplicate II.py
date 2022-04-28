# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
#         dictStore = {}
        
#         for i in range(len(nums)):
            
#             if dictStore.get(nums[i]) != None and abs(dictStore.get(nums[i]) - i) <= k:
#                 return True
            
#             dictStore[nums[i]] = i
                
#         return False

        
    
        # approach 2
        dictStore = {}
        for index, value in enumerate(nums):
            if value in dictStore and abs(index-dictStore.get(value))<=k:
                return True
            dictStore[value] = index
        return False
            
    
    # approach 2 simplified
#     dictStore = {}
#     for index, value in enumerate(nums):

#         if index-k<=dictStore.get(value, -1):
#             return True
#         dictStore[value] = index

#     return Flase