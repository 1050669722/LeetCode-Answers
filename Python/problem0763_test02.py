class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {}
        for i, s in enumerate(S):
            d[s] = i
        # print(d)

        first, last = 0, 0
        ans = []
        for i, s in enumerate(S):
            # last = d[s]
            last = max(last, d[s]) #准确地说，应该是包含当前元素之前的所有元素最后索引的最大值 #否则last会因为元素的改变而变小
            if last == i: #否则说明当前元素s后面还会出现，要不做任何操作继续下去
                ans.append(last - first + 1)
                first = last + 1
        
        return ans
