class Solution:
    def minimumOperations(self, leaves: str) -> int:
        # from collections import Counter
        # d = Counter(leaves)
        
        def isYellow(leaf):
            if leaf == 'y':
                return 1
            else:
                return 0

        def isRed(leaf):
            if leaf == 'r':
                return 1
            else:
                return 0
        
        tmp = [[0, 0, 0] for _ in range(len(leaves))] #行表示秋叶索引，列表示状态序号

        # 第0状态
        tmp[0][0] = isYellow(leaves[0])
        for i, leaf in enumerate(leaves):
            if i < 1:
                continue
            # print(i, leaf)
            tmp[i][0] = tmp[i - 1][0] + isYellow(leaf)
        # print(tmp)

        # 第1状态
        # tmp[1][1] = min(tmp[0][0], tmp[0][1]) + isRed(leaves[1])
        tmp[1][1] = tmp[0][0] + isRed(leaves[1])
        for i, leaf in enumerate(leaves):
            if i < 2:
                continue
            tmp[i][1] = min(tmp[i - 1][0], tmp[i - 1][1]) + isRed(leaf)

        # 第2状态
        # tmp[2][2] = min(tmp[1][1], tmp[1][2]) + isYellow(leaves[2])
        tmp[2][2] = tmp[1][1] + isYellow(leaves[2])
        for i, leaf in enumerate(leaves):
            if i < 3:
                continue
            tmp[i][2] = min(tmp[i - 1][1], tmp[i - 1][2]) + isYellow(leaf)
        # print(tmp)

        return tmp[len(leaves) - 1][2]


