# import os
class Solution:
    def islandPerimeter(self, grid: list) -> int:
        ans = 0
        for p in range(len(grid)):
            for q in range(len(grid[0])):
                # print('---',p,q,'---')
                if grid[p][q] == 1:
                    tmp = self.fun(grid, p, q)
                    # print(tmp)
                    ans += tmp
                # else:
                #     print(0)
                # if p == 0 and q == 1:
                #     os.system('pause')
        return ans*2
    
    def fun(self, grid, p, q):
        res = 0
        if p-1 >= 0:
            if grid[p-1][q] == 0:
                res += 1
                # print('n1')
        else:
            res += 1
            # print('n2')
        if q-1 >= 0:
            if grid[p][q-1] == 0:
                res += 1
                # print('w1')
        else:
            res += 1
            # print('w2')
        # try:
        #     if grid[p+1][q] == 0:
        #         res += 1
        #         # print('s1')
        # except:
        #     res += 1
        #     # print('s2')
        # try:
        #     if grid[p][q+1] == 0:
        #         res += 1
        #         # print('e1')
        # except:
        #     res += 1
        #     # print('e2')
        return res

# solu = Solution()
# grid = [[0,1,0,0],
#         [1,1,1,0],
#         [0,1,0,0],
#         [1,1,0,0]]
# print(solu.islandPerimeter(grid))


