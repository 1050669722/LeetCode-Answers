class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list:
        if x == 1 and y == 1:
            if bound >= 2:
                return [2]
            else:
                return []

        if x != 1 and y == 1:
            import numpy as np
            ans = []
            log_x = np.log(bound)/np.log(x)
            log_x = int(log_x)+1
            for i in range(log_x):
                tmp = x**i + 1
                if tmp <= bound:
                    ans.append(tmp)
            return list(set(ans))
            
        if x == 1 and y != 1:
            import numpy as np
            ans = []
            log_y = np.log(bound)/np.log(y)
            log_y = int(log_y)+1
            for j in range(log_y):
                tmp = 1 + y**j
                if tmp <= bound:
                    ans.append(tmp)
            return list(set(ans))

        if x != 1 and y != 1:
            import numpy as np
            ans = []
            log_x, log_y = np.log(bound)/np.log(x), np.log(bound)/np.log(y)
            log_x, log_y = int(log_x)+1, int(log_y)+1
            for i in range(log_x):
                for j in range(log_y):
                    tmp = x**i + y**j
                    if tmp <= bound:
                        ans.append(tmp)
            return list(set(ans))

solu = Solution()
x, y, bound = 2, 3, 10
x, y, bound = 2, 1, 10
print(solu.powerfulIntegers(x, y, bound))

