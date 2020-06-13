import math
from typing import List

# import time
# import random

# time0 = time.perf_counter()
# for _ in range(100000):
#     ans = random.randint(1, 1000000) / random.randint(1, 1000000)
#     ans = int(random.randint(1, 1000000) / random.randint(1, 1000000))
# print(time.perf_counter() - time0)

# time0 = time.perf_counter()
# for _ in range(100000):
#     ans = random.randint(1, 1000000) % random.randint(1, 1000000)
# print(time.perf_counter() - time0)

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        num = math.sqrt(area)
        # if num == int(num):
        if area % num == 0:
            return [int(num), int(num)]
        else:
            # print(num)
            num = int(num) + 1
            # print(num)
            for k in range(num, area+1):
                # print("k = ", k)
                # print(area / num, int(area / num))
                # if area / k == int(area / k):
                if area % k == 0:
                    # print('num = ', num)
                    return [k, area//k]

# class Solution(object):
#     import math
#     def constructRectangle(self, area):
#         """
#         :type area: int
#         :rtype: List[int]

#         """
#         W = int(math.sqrt(area))        
#         while area%W != 0:
#             W -= 1 
#         return [area//W,W]

# 作者：soramuou
# 链接：https://leetcode-cn.com/problems/construct-the-rectangle/solution/dui-zhe-ge-shu-kai-fang-ran-hou-wang-shang-di-zeng/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

solu = Solution()
area = 3
area = 9999991
print(solu.constructRectangle(area))