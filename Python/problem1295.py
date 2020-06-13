from typing import List
import numpy as np
import math

# def digit_is_even(x):
#     # return ( int(np.log(x+1)/np.log(10)) + 1 ) % 2 == 0

#     # return ( int(np.log(x)/np.log(10)) + 1 ) % 2 == 0

#     # count = 0
#     # while x:
#     #     count += 1
#     #     x //= 10
#     # return count % 2 == 0

#     return len(str(x)) % 2 == 0

# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         ans = 0
#         for num in nums:
#             if digit_is_even(num):
#                 ans += 1
#         return ans


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # return sum(1 for num in nums if len(str(num)) % 2 == 0 )
        # return sum( 1 for num in nums if int(np.log(num)/np.log(10) + 1) % 2 == 0 )
        # return sum( 1 for num in nums if int(math.log10(num) + 1) % 2 == 0 )
        return sum( 1 for num in nums if int(math.log(num, 10) + 1) % 2 == 0 )

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits/solution/tong-ji-wei-shu-wei-ou-shu-de-shu-zi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。