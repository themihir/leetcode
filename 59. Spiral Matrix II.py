# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        if n<1:
            return []
        row_s, col_s, row_e, col_e = 0, 0, n-1, n-1
        count = 1
        while row_s<=row_e and col_s<=col_e:
            #forward
            for i in range(col_s, col_e+1):
                matrix[row_s][i] = count
                count+=1
            row_s += 1
            
            #down
            for i in range(row_s, row_e+1):
                matrix[i][col_e] = count
                count+=1
            col_e -= 1
            
            #reverse
            if (row_s <= row_e):
                for i in range(col_e, col_s-1, -1):
                    matrix[row_e][i] = count
                    count+=1
                row_e -= 1
            
            #up
            if (col_s <= col_e):
                for i in range(row_e, row_s-1, -1):
                    matrix[i][col_s] = count
                    count+=1
                col_s += 1
            
        return matrix