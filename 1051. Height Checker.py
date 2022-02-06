# A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

# You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

# Return the number of indices where heights[i] != expected[i].

 

# Example 1:

# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.
# Example 2:

# Input: heights = [5,1,2,3,4]
# Output: 5
# Explanation:
# heights:  [5,1,2,3,4]
# expected: [1,2,3,4,5]
# All indices do not match.
# Example 3:

# Input: heights = [1,2,3,4,5]
# Output: 0
# Explanation:
# heights:  [1,2,3,4,5]
# expected: [1,2,3,4,5]
# All indices match.
 

# Constraints:

# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100


# solotuon 1st perform count sort to get sorted array and then compares with original array to return count places
# algorithm achieve O(n) time complexity.

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        [1,1,4,2,1,3]
        
        [1,1,1,2,3,4]
        
        m = max(heights)+1
        lenheights = len(heights)
        
        temp = [0]* m
        output = [0] * lenheights
        
        for i in range(lenheights):
            temp[heights[i]] += 1
            
        for i in range(1, m):
            temp[i] += temp[i-1]
            
        for i in range(lenheights-1, -1, -1):
            output[temp[heights[i]]-1] = heights[i]
            temp[heights[i]] -= 1
            
        count = 0
        for i in range(lenheights):
            if heights[i] != output[i]:
                count += 1
        
        return count