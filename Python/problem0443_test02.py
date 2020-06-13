from typing import List

# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         if not chars:
#             return 0

#         count = 1
#         for k in range(1, len(chars)):
#             if chars[k] != chars[k-1]:
#                 if count != 1:

#             else:
#                 continue
        
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        if len(chars) == 1:
            return 1

        count = 1
        ans = []
        for k in range(1, len(chars)):
            tmp = chars[k]
            if tmp != chars[k-1]:
                ans.append(chars[k-1])
                if count != 1:
                    count = list(str(count))
                    ans += count
                else:
                    pass
                count = 1
            else:
                count += 1
        ans.append(tmp)
        if count != 1:
            count = list(str(count))
            ans += count
        else:
            pass
        
        chars = ans
        del ans
        print(chars)

        # return ans
        return len(chars)
        
        
solu = Solution()
chars = ["a","a","b","b","c","c","c"]
# chars = ['a', 'b', 'c', 'd']
# chars = ["a"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(solu.compress(chars))