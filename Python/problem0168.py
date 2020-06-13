class Solution:
    def convertToTitle(self, n: int) -> str:
        d = {}
        for k in range(1, 26+1):
            if k == 1:
                d[k] = 'A'
            else:
                d[k] = chr(ord('A') + (k-1))
        Q = n // 26
        R = n % 26
        
        
        return 

# solu = Solution()
# n = 1
# print(solu.convertToTitle(n))
