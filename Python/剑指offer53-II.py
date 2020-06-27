class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        check = set(range(n))
        return list((check - set(nums)))[0]
        
