class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 1:
        #     return 1 if nums[0] == target else 0
        tmp = []
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                tmp.append(m)
                if i < len(nums) and nums[i] == target:
                    tmp.append(i)
                i += 1
            elif nums[m] > target:
                j = m - 1 
                if j >= 0 and nums[j] == target:
                    tmp.append(j)
            else:
                i = m + 1
                if i < len(nums) and nums[i] == target:
                    tmp.append(i)
        return len(set(tmp))
