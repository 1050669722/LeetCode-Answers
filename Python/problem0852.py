class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not A:
            return None

        #前向差分
        for k in range(1, len(A)-1):
            if A[k-1]<A[k] and A[k]>A[k+1]:
                return k
        return None

        #最大值
        return A.index(max(A))
        
        #二分查找
        p, q = 0, len(A)-1
        while p < q:
            k = (p+q) // 2
            if A[k-1]<A[k]<A[k+1]:
                p = k+1
            elif A[k-1]>A[k]>A[k+1]:
                q = k-1
            else:
                return k
        return p


