class Solution:
    def replaceSpace(self, s: str) -> str:
        # return s.replace(' ', '%20')
        
        ans = []
        for letter in s:
            if letter == ' ':
                ans.append('%20')
            else:
                ans.append(letter)
        return ''.join(ans)

solu = Solution()
s = "We are happy."
s = '    '
ans = solu.replaceSpace(s)
print(ans)