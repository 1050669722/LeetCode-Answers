class Solution:
    def permute(self, nums: list) -> list:
        # ans = []
        # n = len(nums)

        # tmp = []
        # def backtrack(nums):
        #     for k in range(len(nums)):
        #         tmp.append(nums[k])
        #         if len(tmp) == n:
        #             ans.append(tmp)
        #             tmp = []
        #             return
        #         else:
        #             backtrack(nums[k+1:])
        #             return

        # backtrack(nums)
        # return ans

        '''
        什么是全排列
        所谓全排列，无非就是各个元素一次交换位置
        '''
        ans = []
        n = len(nums)

        def backtrack(first): #数组或者子数组的头元素，时刻在改变
            if first == n:
                ans.append(nums.copy())
                return
            for k in range(first, n): #大数组的交换中 嵌套着 小数组的交换
                nums[first], nums[k] = nums[k], nums[first]
                backtrack(first+1)
                nums[first], nums[k] = nums[k], nums[first] #从函数中出来，还要再交换回来，供后来者使用
            return    

        backtrack(0)
        return ans

        






