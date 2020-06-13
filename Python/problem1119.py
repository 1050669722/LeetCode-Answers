class Solution:
    def removeVowels(self, S: str) -> str:
        s = set(['a','e','i','o','u'])
        ans = []
        for s0 in S:
            if s0 not in s: #在集合中使用in是O(1)的时间复杂度
                ans.append(s0)
        # S = ans
        return ''.join(ans)