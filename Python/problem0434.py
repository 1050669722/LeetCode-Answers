class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


solu = Solution()
s = "Hello, my name is John"
print(solu.countSegments(s))