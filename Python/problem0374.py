# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # if n == 1:
        #     return 1
        i, j = 1, n
        while i <= j:
            m = (i + j) // 2
            # print('m: {}'.format(m))
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                i = m + 1
            else:
                j = m - 1
