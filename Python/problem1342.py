class Solution:
    def numberOfSteps (self, num: int) -> int:
        
        def fun(num, res): #定义
            if num != 0:
                if num % 2 == 0:
                    num //= 2
                    res += 1
                    num, res = fun(num, res)
                else:
                    num -= 1
                    res += 1
                    num, res = fun(num, res)
            else:
                None
            return num, res
        
        res = 0
        _, res = fun(num, res) #调用
        return res

solu = Solution()
num = 14
ans = solu.numberOfSteps(num)
print(ans)