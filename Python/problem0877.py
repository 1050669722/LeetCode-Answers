class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        dp也可以写成函数，也可以写成数组，
        要么是递归，要么是递推，
        按照方便的来,
        递归是从大到小，递推是从小到大；
        但是这里更加值得注意的是 问题的建模方式
        dp成为了净胜分，
        它与两个序号都有关系，
        所以应该写成dp[i, j]或dp[i][j]
        '''
        N = len(piles)

        def dp(i, j):
            if i > j:
                return 0 #递归结束的条件，这是一个边界
            parity = (j - i - N) % 2 #表示第几次进入这个函数的奇偶
            if parity == 1:
                return max(piles[i]+dp(i+1, j), piles[j]+dp(i, j-1))
            else:
                return min(-piles[i]+dp(i+1, j), -piles[j]+dp(i, j-1))

        return dp(0, N-1) > 0

        # return True




