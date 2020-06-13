class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS, stackT = [], []
        for k in range(len(S)):
            if S[k] == '#':
                try:
                    stackS.pop()
                except:
                    pass
            else:
                stackS.append(S[k])
        for k in range(len(T)):
            if T[k] == '#':
                try:
                    stackT.pop()
                except:
                    pass
            else:
                stackT.append(T[k])
        return stackS == stackT

