from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        ans = []
        if n == 1:
            ans.append('0')
        start, end = 10**(n-1), 10**n-1
        for num in range(start, end+1):
            tmp = str(num)
            if self.isStrobogrammatic(tmp):
                ans.append(tmp)
        return ans

    def isStrobogrammatic(self, num: str) -> bool:
        if len(num) == 1:
            return num == '0' or num == '8' or num == '1'
        if num[-1] == '0':
            return False
        d = {'0':'0', '6':'9', '8':'8', '9':'6', '1':'1'}
        tmp = list(num)
        for k in range(len(tmp)):
            try:
                tmp[k] = d[tmp[k]]
            except:
                return False
        tmp.reverse()
        return num == ''.join(tmp)


solu = Solution()
n = 7
print(solu.findStrobogrammatic(n))