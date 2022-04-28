# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_s, col_s, row_e, col_e = 0, 0, len(matrix)-1, len(matrix[0])-1
        result = []
        if len(matrix)==0:
            return result
        
        while row_s<=row_e and col_s<=col_e:
            #forward
            for i in range(col_s, col_e+1):
                result.append(matrix[row_s][i])
            row_s += 1
            
            #down
            for i in range(row_s, row_e+1):
                result.append(matrix[i][col_e])
            col_e -= 1
            
            #reverse
            if (row_s <= row_e):
                for i in range(col_e, col_s-1, -1):
                    result.append(matrix[row_e][i])
                row_e -= 1
            
            #up
            if (col_s <= col_e):
                for i in range(row_e, row_s-1, -1):
                    result.append(matrix[i][col_s])
                col_s += 1
            
        return result
            

# solution: https://leetcode.com/problems/spiral-matrix/discuss/394774/python-3-solution-for-spiral-matrix-one-of-the-most-easiest-you-will-never-forget      

# one line solution: https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
# def spiralOrder(self, matrix):
#     return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])