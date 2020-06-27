class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # d = {}
        # arr.sort(key=lambda x: abs(x), reverse=True)
        # for i, a in enumerate(arr):
        #     if 2 * a in d:
        #         return True
        #     else:
        #         d[a] = i
        # return False

        d = set()
        arr.sort(key = lambda x: abs(x), reverse=True)
        for a in arr:
            if 2 * a in d:
                return True
            else:
                d.add(a)
        return False
        
