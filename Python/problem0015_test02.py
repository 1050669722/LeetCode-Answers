class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort() #排序，则重复元素必出现在相邻位置
        ans = []

        for first in range(0, len(nums), 1): #排序和双指针，去除了一层复杂度
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
