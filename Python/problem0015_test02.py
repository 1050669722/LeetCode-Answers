class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        ans = []

        for first in range(0, len(nums), 1):
            if nums[first] == nums[first - 1] and first > 0:
                continue
            
            third = len(nums) - 1

            for second in range(first + 1, third):
                if nums[second] == nums[second - 1] and second > first + 1:
                    continue
                
                while second < third and nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                
                if second == third:
                    break
                if nums[first] + nums[second] + nums[third] < 0:
                    continue
                if nums[first] + nums[second] + nums[third] == 0:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans
