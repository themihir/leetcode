# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # approach 1 (self):
#         if len(s)!=len(t):
#             return False
        
#         temp = {}
#         for val in s:
#             temp[val] = temp.get(val, 0)+ 1
            
#         for val in t:
#             if temp.get(val,-1)>0:
#                 temp[val] = temp.get(val)-1
#             else:
#                 return False
#         return True
                
        
        # approach 2: neetcode
#         if len(s) != len(t):
#             return False
        
#         d1, d2 = {}, {}
        
#         for i in range(len(s)):                       
#             d1[s[i]] = d1.get(s[i], 0)+1
#             d2[t[i]] = d2.get(t[i], 0)+1
            
            
#         for val in d1:            
#             if d1[val] != d2.get(val, 0):
#                 return False
#         return True
    
        # approach 3
        # import collections 
        # s_count = collections.Counter(s)
        # t_count = collections.Counter(t)
        # return s_count == t_count
        
        # approach 4:
        if(len(s)!=len(t)):
            return False
        remove_dup = set(s)
        for val in remove_dup:
            if s.count(val) != t.count(val):
                return False
        return True