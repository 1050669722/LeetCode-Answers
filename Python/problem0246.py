class Solution:
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
num = '69'
num = '88'
num = '962'
num = '1'
print(solu.isStrobogrammatic(num))