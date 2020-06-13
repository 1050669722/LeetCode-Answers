from collections import deque

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set(('a','e','i','o','u','A','E','I','O','U'))
        words = S.split(' ')
        for k, word in enumerate(words):
            word = deque(word)
            if word[0] in vowel:
                word.append('ma')
            else:
                tmp = word.popleft()
                word.append(tmp+'ma')
            word.append('a'*(k+1))
            words[k] = ''.join(word)
        return ' '.join(words)

S = "I speak Goat Latin"
S = "The quick brown fox jumped over the lazy dog"
solu = Solution()
print(solu.toGoatLatin(S))