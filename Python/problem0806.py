from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        d = {}
        for k, w in enumerate(widths):
            d[chr(ord('a')+k)] = w
        # print(d)
        rownum = 1
        count = 0
        for s in S:
            count += d[s]
            if count > 100:
                rownum += 1
                count = d[s]
            else:
                pass
        # return [rownum, count]
        return rownum, count

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
solu = Solution()
print(solu.numberOfLines(widths, S))