class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) <= 1:
            return []
        ans = []
        keys = set(A[0])
        for k in keys:
            tmp = min(a.count(k) for a in A)
            for _ in range(tmp):
                ans.append(k)
        return ans

