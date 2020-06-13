from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if not letters:
            return None
        p, q = 0, len(letters)-1
        m = (p+q) // 2
        while p < q:
            if letters[m] == target:
                # try:
                #     # return letters[m+1]
                for k in range(m+1, len(letters)):
                    if letters[k] > target:
                        return letters[k]
                return letters[0]
                # except:
                #     return letters[0]
            elif letters[m] < target:
                p = m + 1
                m = (p+q) // 2
            else:
                q = m - 1
                m = (p+q) // 2
        # print(p, q, m)
        if letters[p] > target:
            return letters[p]
        else:
            try:
                return letters[p+1]
            except:
                return letters[0]

solu = Solution()
# letters, target = ["c", "f", "j"], "a"
# letters, target = ["c", "f", "j"], "c"
# letters, target = ["c", "f", "j"], "d"
# letters, target = ["c", "f", "j"], "g"
# letters, target = ["c", "f", "j"], "j"
letters, target = ["c", "f", "j"], "k"
print(solu.nextGreatestLetter(letters, target))