# class Solution:
#     def decodeString(self, s: str) -> str:
#         from collections import defaultdict
#         stack = []
#         mark = 0
#         d_nums = defaultdict(list)
#         d_letters = defaultdict(list)
#         # nums = [] #存储方括号前的数字
#         # letters = [] #存储方括号中的字符
#         for k in range(len(s)):
#             if s[k] == '[':
#                 # mark += 1
#                 # print(d_nums[mark])
#                 tmp = int(''.join(d_nums[mark]))
#                 d_nums[mark] = []
#                 d_nums[mark].append(tmp)
#                 # print(d_nums[mark])
#                 del tmp
#             elif s[k] == ']':
#             # if s[k] == ']':
#                 mark -= 1
#                 # print('mark: ', mark)
#                 # print(d_nums[mark+1])
#                 if mark == 0:
#                     for _ in range(d_nums[mark+1][0]):
#                         stack.append(''.join(d_letters[mark+1]))
#                 else:
#                     for _ in range(d_nums[mark+1][0]):
#                         d_letters[mark].append(''.join(d_letters[mark+1]))
#                 # print(d_nums)
#                 # print(d_letters)
#                 d_letters[mark+1] = []
#                 d_nums[mark+1] = []
#                 # print(stack)
#             elif s[k].isdigit():
#                 # if d_nums[mark] == []:
#                 if k-1 >= 0:
#                     if not s[k-1].isdigit():
#                         mark += 1
#                 else:
#                     mark += 1
#                 # d_nums[mark].append(int(s[k]))
#                 d_nums[mark].append(s[k])
#             elif mark == 0:
#                 stack.append(s[k])
#             elif s[k] != '[':
#                 d_letters[mark].append(s[k])
#             # if mark != 0:
#             #     if s[k].isdigit():
#             #         nums.append(int(s[k]))
#             #     elif s[k] == '[':
#             #         mark += 1
#             #     elif s[k] == ']':
#             #         mark -= 1
#             #     elif mark == 0:
#             #         stack.append(s[k])
#         # print(stack)
#         return ''.join(stack)

# # solu = Solution()
# # # s = "3[a]2[bc]"
# # # s = "3[a2[c]]"
# # # s = "2[abc]3[cd]ef"
# # s = "100[leetcode]"
# # print(solu.decodeString(s))


class Solution:
    def decodeString(self, s: str) -> str:
        from collections import defaultdict
        stack = []
        mark = 0
        d_nums = defaultdict(list)
        d_letters = defaultdict(list)
        for k in range(len(s)):
            if s[k] == '[':
                tmp = int(''.join(d_nums[mark]))
                d_nums[mark] = []
                d_nums[mark].append(tmp)
                del tmp
            elif s[k] == ']':
                mark -= 1
                if mark == 0:
                    for _ in range(d_nums[mark+1][0]):
                        stack.append(''.join(d_letters[mark+1]))
                else:
                    for _ in range(d_nums[mark+1][0]):
                        d_letters[mark].append(''.join(d_letters[mark+1]))
                d_letters[mark+1] = []
                d_nums[mark+1] = []
            elif s[k].isdigit():
                if k-1 >= 0:
                    if not s[k-1].isdigit():
                        mark += 1
                else:
                    mark += 1
                d_nums[mark].append(s[k])
            elif mark == 0:
                stack.append(s[k])
            elif s[k] != '[':
                d_letters[mark].append(s[k])
        return ''.join(stack)

# solu = Solution()
# # s = "3[a]2[bc]"
# # s = "3[a2[c]]"
# # s = "2[abc]3[cd]ef"
# s = "100[leetcode]"
# print(solu.decodeString(s))


class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res

# # 作者：jyd
# # 链接：https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
