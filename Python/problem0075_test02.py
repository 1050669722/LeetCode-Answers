class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ans = []
        
        tmp = [0] * (max(nums) + 1)
        
        for num in nums:
            tmp[num] += 1
        
        count = 0
        for k in range(len(tmp)):
            for _ in range(tmp[k]):
                nums[count] = k
                count += 1
                # ans.append(k)
        
        # print(ans)
        # nums = ans
        # return None
