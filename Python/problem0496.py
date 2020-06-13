# from typing import List

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         ans = [-1] * len(nums1)
#         tmp_nums1 = nums1.copy()
#         nums1 = set(nums1)
#         for k, num in enumerate(nums2):
#             if num in nums1:
#                 for p in range(k+1, len(nums2)):
#                     if nums2[p] > num:
#                         ind = tmp_nums1.index(num)
#                         ans[ind] = nums2[p]
#                         break
#         return ans

# solu = Solution()
# nums1, nums2 = [4,1,2], [1,3,4,2]
# print(solu.nextGreaterElement(nums1, nums2))


from typing import List

class Solution():
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


        