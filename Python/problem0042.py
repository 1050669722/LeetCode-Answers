class Solution:
    def trap(self, height: list) -> int:
        if len(height) <= 2:
            return 0
        if len(height) == 3:
            if height[0] > height[1] and height[1] < height[2]:
                tmp = min(height[0], height[2])
                return tmp - height[1]
            else:
                return 0
        
        ans = 0
        # p, q = 0, 2
        # while q < len(height)-1:
        #     if height[p-1] < height[p] or p-1 < 0:
        #         if :
        #     else:
        #         p += 1
        
        # while True:
        for _ in range(100):
            points = []
            if height[0] > height[1]:
                points.append(0)
            for k in range(1, len(height)-1):
                # if (height[k-1] < height[k] or k-1 < 0) and (height[k] < height[k+1] or k+1 > len(height)-1):
                if ((height[k-1] <= height[k]) and (height[k] > height[k+1])) or ((height[k-1] < height[k]) and (height[k] >= height[k+1])):
                    points.append(k)
            if height[len(height)-1] > height[len(height)-2]:
                points.append(len(height)-1)
            # if len(points) <= 1:
            #     break
            # print(points)

            for i in range(len(points)-1): #这虽然是一个二重循环，但是时间复杂度应该还是O(n)
                p, q = points[i], points[i+1]
                # print(p, q)
                tmp = min(height[p], height[q])
                for j in range(p+1, q):
                    ans += max(tmp - height[j], 0)
                    height[j] = max(height[j], tmp)
            # print(height)
        return ans

# solu = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# # height = [0,1,0]
# # height = [0]
# # height = [1,0,2]
# # height = [5,4,1,2]
# # height = [5,2,1,2,1,5]
# height = [4,2,0,3,2,4,3,4]
# print(solu.trap(height))



