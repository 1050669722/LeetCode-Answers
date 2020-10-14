class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # ans = set(A[0])
        # for string in A[1:]:
        #     ans &= set(string)
        # return list(ans) #如果是这样的话，就不包含重复字符了


        # from collections import Counter
        
        # def update(Dict, tmp):
        #     for k, v in tmp.items():
        #         if k in Dict and v < Dict[k]:
        #             Dict[k] = v
        #     return Dict

        # Dict = Counter(A[0])
        # for string in A[1:]:
        #     tmp = Counter(string)
        #     Dict = update(Dict, tmp)

        # return list(Dict.keys()) #后来的字符串只是不给其增加


        from collections import Counter
        import sys

        letters = set(A[0])
        for string in A[1:]:
            letters &= set(string)
        
        ans = dict()
        for letter in letters:
            ans[letter] = sys.maxsize
        for string in A:
            tmp = Counter(string)
            for k, v in tmp.items():
                if k in ans:
                    ans[k] = min(ans[k], v)
        
        res = []
        for k, v in ans.items():
            for _ in range(v):
                res.append(k)
        
        return res

