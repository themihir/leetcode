# 253. Meeting Rooms II
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

# Difficulty:
# Medium
# Lock:
# Prime

# solution 1:

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        starters = sorted([i.start for i in intervals])
        enders = sorted([i.end for i in intervals])

        sp, ep = 0, 0
        count, maxc = 0, 0

        while sp<len(starters):
            if starters[sp]<enders[ep]:
                count+=1
                sp+=1
            else:
                count-=1
                ep+=1
            maxc =max(maxc, count)
        return maxc


# solution 2

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        arr = []
        for i in intervals:
            arr.append([i.start, 1])
            arr.append([i.end, -1])
        arr.sort(key=lambda x: x[0])

        count = 0
        maxc = 0
        for i in arr:
            if i[1]==1:
                count+=1
            else:
                count-=1
            maxc = max(maxc, count)
        return maxc