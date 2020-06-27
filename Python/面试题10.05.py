class Solution:
    def findString(self, words: List[str], s: str) -> int:
        try:
            return words.index(s)
        except:
            return -1

        # for i, word in enumerate(words):
        #     if s == word:
        #         return i
        # return -1

        # 如果用二分查找，应该怎样做呢？
