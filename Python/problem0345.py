class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', }
        s = list(s)
        p, q = 0, len(s)-1
        while p < q:
            while p < q and s[p] not in vowels:
                p += 1
            while p < q and s[q] not in vowels:
                q -= 1
            s[p], s[q] = s[q], s[p]
            p += 1
            q -= 1
        return ''.join(s)

solu = Solution()
s = "hello"
print(solu.reverseVowels(s))