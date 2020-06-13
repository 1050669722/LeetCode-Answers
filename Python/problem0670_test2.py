class Solution:
    def maximumSwap(self, num: int) -> int:
        num1 = list(str(num))
        num2 = sorted(num1, reverse = True)
        if num1 == num2:
            return num

        # 找到与最大数字之间的最主要差异
        for k in range(len(num1)):
            if num1[k] != num2[k]:
                break
        
        # print(num1[k], num2[k])
        # p = num1.index(num2[k]) #得找到最后一个而不是第一个
        # for p in range(len(num1)-1, -1, -1):
        #     if num1[p] == num2[k]:
        #         break
        
        p = -(num1[::-1].index(num2[k]) + 1)# + len(num1)

        num1[k], num1[p] = num1[p], num1[k]

        return int(''.join(num1))


solu = Solution()
num = 2736
# num = 9973
num = 98368
print(solu.maximumSwap(num))