# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i < j:
            m = (i + j) // 2
            if isBadVersion(m) == True:
                j = m
            else:
                i = m + 1
        idx = min(i, j)
        return idx #在这一题当中，直接返回i也是可以的 #整除舍去的做法不会让m偏向大的一方，所以i = m + 1不会让i跑到j的右方
