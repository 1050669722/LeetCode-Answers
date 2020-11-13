class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # ans = []
        # for ele in zip(nums[:len(nums) // 2], nums[len(nums) // 2:]):
        #     ans += ele
        # return ans
        
        nums[::2],nums[1::2]=nums[:n],nums[n:]
        return nums
        
        # 应该还有额外空间为O(1)的办法
        
