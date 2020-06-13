class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        v1, v2= [int(x) for x in v1], [int(x) for x in v2]
        lendiff = len(v1) - len(v2)
        # print(lendiff)
        # print(v1, v2)
        if lendiff > 0:
            for _ in range(lendiff):
                v2.append(0)
        elif lendiff < 0:
            for _ in range(-lendiff):
                v1.append(0)
        # print(v1, v2)
        ans = 0
        for k in range(len(v1)):
            if v1[k] > v2[k]:
                ans = 1
                break
            elif v1[k] < v2[k]:
                ans = -1
                break
        return ans

solu = Solution()
version1, version2 = "0.1", "1.1"
# version1, version2 = "1.0.1", "1"
# version1, version2 = "7.5.2.4", "7.5.3"
version1, version2 = "1", "1.1"
version1, version2 = "01", "1"
print(solu.compareVersion(version1, version2))

