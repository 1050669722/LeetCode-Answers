from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # d = {}
        # d[first] = second
        # text = text.split()
        # ans = []
        # for k in range(len(text)-2):
        #     if text[k] in d:
        #         if text[k+1] == d[text[k]]:
        #             ans.append(text[k+2])
        #         else:
        #             pass
        #     else:
        #         pass
        # return ans

        text = text.split()
        tmp = zip(text, text[1:], text[2:])
        ans = []
        for e in tmp:
            if e[0] == first and e[1] == second:
                ans.append(e[2])
        return ans

text = 'alice is a good girl she is a good student'
first = 'a'
second = 'good'
text = 'we will we will rock you'
first = 'we'
second = 'will'
solu = Solution()
print(solu.findOcurrences(text, first, second))