class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # count = 0
        # for a1 in arr1:
        #     tmp = 0
        #     for a2 in arr2:
        #         if abs(a1 - a2) > d:
        #             tmp += 1
        #     if tmp == len(arr2):
        #         count += 1
        # return count

        arr2.sort()
        count = 0
        for a1 in arr1:
            idx = self.fun(a1, arr2)
            # print(idx)
            if 0 < idx < len(arr2) and arr2[idx] == a1:
                if 0 > d:
                    count += 1
            elif idx == 0:
                if arr2[idx] - a1 > d:
                    count += 1
            elif idx == len(arr2):
                if a1 - arr2[idx - 1] > d:
                    count += 1
            elif 0 < idx < len(arr2):
                if a1 - arr2[idx - 1] > d and arr2[idx] - a1 > d:
                    count += 1
        return count

    def fun(self, a, nums):
        '''
        a在升序数组nums中应该排第几
        '''
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] < a:
                i = m + 1
            elif nums[m] > a:
                j = m - 1
            else:
                return m
        
        idx = min(i, j)
        
        if idx < 0:
            return 0
        if idx > len(nums) - 1:
            return (len(nums) - 1) + 1
        if nums[idx] < a:
            return idx + 1
        else:
            return (idx - 1) + 1
            
