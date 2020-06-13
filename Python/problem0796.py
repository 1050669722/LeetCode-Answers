class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        A = [x for x in A]
        B = [x for x in B]
        from collections import deque
        A = deque(A)
        B = deque(B)
        for _ in range(len(A)):
            tmp = A.popleft()
            A.append(tmp)
            # print(A)
            if A == B:
                return True
        return False

solu = Solution()
A, B = 'abcde', 'cdeab'
print(solu.rotateString(A, B))
