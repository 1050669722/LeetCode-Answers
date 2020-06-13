class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        ans = 0
        for k in range(len(guess)):
            if guess[k] == answer[k]:
                ans += 1
        return ans


