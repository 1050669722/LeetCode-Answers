class Solution:
    def findLength(self, A: list, B: list) -> int:
        # dp = [ [0]*len(A) for _ in range(len(B)) ]
        # for k in range(len(A)):
        #     dp[0][k] = int(A[k] == B[0])
        # for k in range(len(B)):
        #     dp[k][0] = int(B[k] == A[0])
        # # print(dp)
        # for i in range(1, len(B)):
        #     for j in range(1, len(A)):
        #         # print(dp[i][j])
        #         # print(B[i], A[j])
        #         # print(dp[i-1][j], dp[i][j-1])
        #         dp[i][j] = min( int(B[i] == A[j]) + max(dp[i-1][j], dp[i][j-1]), i+1, j+1 )
        # print(dp)
        # return dp[-1][-1]

        dp = [ [0]*(len(A)+1) for _ in range(len(B)+1) ]
        for i in range(len(B)-1, -1, -1):
            for j in range(len(A)-1, -1, -1):
                if B[i] == A[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        # print(dp)
        # return max( (max(row) for row in dp) ) #迭代器
        return max( [max(row) for row in dp] ) #列表

# solu = Solution()
# A, B = [1,2,3,2,1], [3,2,1,4,7]
# A, B = [0,0,0,0,0], [0,0,0,0,0]
# A, B = [0,1,1,1,1], [1,0,1,0,1]
# print(solu.findLength(A, B))