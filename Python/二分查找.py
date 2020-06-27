'''
二分查找
bisect.bisect_left(nums, num)
'''

def fun(self, a, nums):
    '''
    a在升序数组nums中应该排第几
    '''
    i, j = 0, len(nums) - 1 #根据问题情境，这里需要考虑是否需要-1
    while i < j: #根据问题情境，这里需要考虑是否需要=
        m = (i + j) // 2 #每轮都应该更新中间指针
        if nums[m] < a:
            i = m + 1
        elif nums[m] > a:
            j = m - 1
        else:
            return m
        # print('i:{}, j:{}'.format(i, j))
    
    idx = min(i, j)
    
    if idx < 0:
        return 0
    if idx > len(nums) - 1:
        return (len(nums) - 1) + 1
    if nums[idx] < a:
        return idx + 1
    else:
        return (idx - 1) + 1
