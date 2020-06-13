# class Solution:
#     def sumEvenAfterQueries(self, A: list, queries: list) -> list:
#         ans = []
#         A[queries[0][1]] += queries[0][0]
#         Sum = 0
#         for a in A:
#             if a % 2 == 0:
#                 Sum += a
#         ans.append(Sum)
#         tmp_last = A[queries[0][1]]
#         # print(A)
#         for k in range(1, len(queries)):
#             # tmp_current = A[queries[k][1]] + queries[k][0]
#             # A[queries[k][1]] = tmp_current
#             A[queries[k][1]] += queries[k][0]
#             tmp_current = A[queries[k][1]]
#             print(tmp_last, tmp_current)
#             # print(A)
#             if tmp_last%2 == 1 and tmp_current%2 == 1:
#                 tmp = ans[-1]
#                 ans.append(tmp)
#             elif tmp_last%2 == 1 and tmp_current%2 == 0:
#                 tmp = tmp_current - 0 + ans[-1]
#                 ans.append(tmp)
#             elif tmp_last%2 == 0 and tmp_current%2 == 1:
#                 tmp = 0 - tmp_last + ans[-1]
#                 ans.append(tmp)
#             else:#if tmp_last%2 == 0 and tmp_current%2 == 0:
#                 tmp = tmp_current - tmp_last + ans[-1]
#                 ans.append(tmp)
#             tmp_last = tmp_current
#         return ans

# solu = Solution()
# A, queries = [1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]
# print(solu.sumEvenAfterQueries(A, queries))


class Solution:
    def sumEvenAfterQueries(self, A: list, queries: list) -> list:
        ans = []
        A[queries[0][1]] += queries[0][0]
        Sum = 0
        for a in A:
            if a % 2 == 0:
                Sum += a
        ans.append(Sum)
        # tmp_last = A[queries[0][1]]
        # print(A)
        for k in range(1, len(queries)):
            # tmp_current = A[queries[k][1]] + queries[k][0]
            # A[queries[k][1]] = tmp_current
            tmp_last = A[queries[k][1]]
            A[queries[k][1]] += queries[k][0]
            tmp_current = A[queries[k][1]]
            # print(tmp_last, tmp_current)
            # print(A)
            if tmp_last%2 == 1 and tmp_current%2 == 1:
                tmp = ans[-1]
                ans.append(tmp)
            elif tmp_last%2 == 1 and tmp_current%2 == 0:
                tmp = tmp_current - 0 + ans[-1]
                ans.append(tmp)
            elif tmp_last%2 == 0 and tmp_current%2 == 1:
                tmp = 0 - tmp_last + ans[-1]
                ans.append(tmp)
            else:#if tmp_last%2 == 0 and tmp_current%2 == 0:
                tmp = tmp_current - tmp_last + ans[-1]
                ans.append(tmp)
            tmp_last = tmp_current
        return ans

# solu = Solution()
# A, queries = [1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]
# print(solu.sumEvenAfterQueries(A, queries))