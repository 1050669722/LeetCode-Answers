from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        max_ = max(A)
        ind = A.index(max_)
        if ind == 0 or ind == len(A)-1:
            return False
        for k in range(ind, -1, -1):
            if k == 0:
                # print(1)
                break
                # return False
            else:
                if A[k-1] < A[k]:
                    pass
                else:
                    return False
        for k in range(ind, len(A)):
            # print(k)
            if k == len(A)-1:
                break
                # return False
            else:
                if A[k] > A[k+1]:
                    pass
                else:
                    return False
        return True

A = [2,1]
# A = [3,5,5]
# A = [0,3,2,1]
A = [2,0,2]
A = [0,1,2,3,4,5,6,7,8,9]
A = [0,3,2,1]
solu = Solution()
print(solu.validMountainArray(A))