class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()
        d = {}
        # print(pattern, str)
        if len(pattern) != len(str):
            return False
        s = set()
        for k in range(len(pattern)):
            if pattern[k] in d:
                if d[pattern[k]] != str[k]:
                    return False
            else:
                if str[k] not in s:
                    d[pattern[k]] = str[k]
                    s.add(str[k])
                else:
                    return False
        return True

solu = Solution()
pattern, str = "jquery", "jquery"
pattern, str = "abba", "dog dog dog dog"
print(solu.wordPattern(pattern, str))