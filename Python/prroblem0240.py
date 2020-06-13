class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # if not matrix or not matrix[0]:
        #     return False
        # row, col = len(matrix)-1, 0
        # while row >= 0 and col <= len(matrix[0])-1:
        #     if matrix[row][col] == target:
        #         return True
        #     if matrix[row][col] > target:
        #         row -= 1
        #     else:
        #         col += 1
        # return False

        if not matrix or not matrix[0]:
            return False
        row, col = 0, len(matrix[0])-1
        while col >= 0 and row <= len(matrix)-1:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

