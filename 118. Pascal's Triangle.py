# 118. Pascal's Triangle

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # Method 1
        # return [[comb(i,j) for j in range(i+1)] for i in range(numRows)]
        
        # Method 2
        # master = []
        # for i in range(numRows):
        #     temp=[0]*(i+1)
        #     temp[0]=temp[-1]=1
        #     for j in range(1, i):
        #         temp[j] = master[i-1][j-1]+master[i-1][j]
        #     master.append(temp)
        # return master

        # Method 3
        master = [[1]]
        
        for i in range(numRows-1):
            temp = [0] + master[-1] + [0]
            row = []
            for j in range(len(master[-1])+1):
                row.append(temp[j]+temp[j+1])
            master.append(row)
        return master