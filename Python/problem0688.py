def isin(N, r, c):
    if 0<=r<=N-1 and 0<=c<=N-1:
        return True
    else:
        return False

def singlePro(N, r, c):
    ans = 0
    if isin(N, r+1, c+2):
        ans += 1
    if isin(N, r+2, c+1):
        ans += 1
    if isin(N, r-1, c-2):
        ans += 1
    if isin(N, r-2, c-1):
        ans += 1
    if isin(N, r+1, c-2):
        ans += 1
    if isin(N, r-1, c+2):
        ans += 1
    if isin(N, r+2, c-1):
        ans += 1
    if isin(N, r-2, c+1):
        ans += 1
    return ans/8

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        ans = 0
        for _ in range(K):
            ans *= singlePro(N, r, c)
            r, c = 



N, K, r, c = 3, 2, 0, 0
solu = Solution()
print(solu.knightProbability(N, K, r, c))