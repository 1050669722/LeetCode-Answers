# class Solution:
#     def rotate(self, nums: list, k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if k <= 0 or not nums:
#             return nums
#         n = len(nums)
#         # mark = 0
#         # if n%2 == 0 and k%2 == 0:
#         #     k += 1
#         #     mark = 1
#         count = 0
#         while n % k == 0:
#             k += 1
#             count += 1
#             # mark = 1
#         p = 0
#         CurrentVal = nums[p]
#         print(nums)
#         for _ in range(n):
#             NewInd = (p+k) % n
#             tmp = nums[NewInd]
#             nums[NewInd] = CurrentVal
#             CurrentVal = tmp
#             p = NewInd
#         print(nums)
#         if count != 0:
#             for _ in range(count):
#                 tmp = nums.pop(0)
#                 nums.append(tmp)
#         return nums

# solu = Solution()
# # nums, k = [1,2,3,4,5,6,7], 3
# # nums, k = [-1,-100,3,99], 2
# nums, k = [1,2,3,4,5,6], 2
# print(solu.rotate(nums, k))


# class Solution:
#     def rotate(self, nums: list, k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if k <= 0 or not nums:
#             return nums
#         n = len(nums)
#         p = 0
#         CurrentVal = nums[p]
#         for _ in range(n):
#             # OldInd = p
#             NewInd = (p+k) % n
#             tmp = nums[NewInd]
#             nums[NewInd] = CurrentVal
#             CurrentVal = tmp
#             p = NewInd
#         return nums

# solu = Solution()
# # nums, k = [1,2,3,4,5,6,7], 3
# # nums, k = [-1,-100,3,99], 2
# nums, k = [1,2,3,4,5,6], 2
# print(solu.rotate(nums, k))


class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k <= 0 or not nums:
            return nums
        n = len(nums)
        tmp = nums.copy()
        for p in range(n):
            NewInd = (p+k) % n
            nums[NewInd] = tmp[p]
        return nums

solu = Solution()
nums, k = [1,2,3,4,5,6,7], 3
# nums, k = [-1,-100,3,99], 2
# nums, k = [1,2,3,4,5,6], 2
print(solu.rotate(nums, k))


