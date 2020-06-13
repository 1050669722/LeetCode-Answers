class Solution:
    def isToeplitzMatrix(self, matrix: list) -> bool:
        # # m = len(matrix) #m行
        # # n = len(matrix[0]) #n列
        # res = matrix[0][:-1]
        # for k, line in enumerate(matrix[1:]):
        #     tmp = line[1:]
        #     if res != tmp:
        #         return False
        #     res = line[:-1]
        # return True

        # res = matrix[0][:-1]
        # for line in matrix[1:]:
        #     tmp = line[1:]
        #     if res != tmp:
        #         return False
        #     res = line[:-1]
        # return True

        for k in range(1, len(matrix)):
            tmp = matrix[k][1:]
            for p in range(len(tmp)):
                if tmp[p] != matrix[k-1][p]:
                    return False
        return True

# solu = Solution()
# matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# print(solu.isToeplitzMatrix(matrix))



