# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        n = len(arr)
        
        while i<n-1 and arr[i]<arr[i+1]:
            i+=1
            
        if i==0 or i==n-1:
            return False
        
        while i<n-1 and arr[i]>arr[i+1]:
            i+=1
        if i==n-1:
            return True