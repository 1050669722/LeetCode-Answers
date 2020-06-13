class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for k, n in enumerate(num):
            if n == '6':
                num[k] = '9'
                return int(''.join(num))
        return int(''.join(num))

solu = Solution()
num = 9669
ans = solu.maximum69Number(num)
print(ans)