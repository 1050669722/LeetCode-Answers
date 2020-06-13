from typing import List
from collections import Counter

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for k, query in enumerate(queries):
            tmp_dict = Counter(query)
            queries[k] = min(tmp_dict.items())[1]
        for k, word in enumerate(words):
            tmp_dict = Counter(word)
            words[k] = min(tmp_dict.items())[1]
        # print(queries, words)
        # 其实更好的办法是排序之后用二分查找
        ans = []
        for query in queries:
            count = 0
            for word in words:
                if query < word:
                    count += 1
            ans.append(count)
        return ans

queries = ["bbb","cc"]; words = ["a","aa","aaa","aaaa"]
solu = Solution()
print(solu.numSmallerByFrequency(queries, words))
        