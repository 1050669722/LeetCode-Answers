class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, t = [], []
        count = 1
        for k in range(1, len(name)):
            if name[k] != name[k-1]:
                n.append(count)
                count = 1
            else:
                count += 1
        n.append(count)
        
        count = 1
        for k in range(1, len(typed)):
            if typed[k] != typed[k-1]:
                t.append(count)
                count = 1
            else:
                count += 1
        t.append(count)

        if len(t) != len(n):
            return False
        else:
            for k in range(len(n)):
                if n[k] > t[k]:
                    return False
            return True

solu = Solution()
name, typed = "alex", "aaleex"
name, typed = "saeed", "ssaaedd"
print(solu.isLongPressedName(name, typed))