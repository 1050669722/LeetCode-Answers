# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:13:32 2019

@author: Administrator
"""

class Solution:
    def isValidSudoku(self, board: list) -> bool:
        temp = [0] * 9
        for k in range(9):
            temp[k] = [0] * 9
#        print(temp)
        for i, L in enumerate(board):
            for j in range(len(L)):
                if '0'<=board[i][j] and board[i][j]<='9':
                    temp[i][j] = int(board[i][j])
                else:
                    temp[i][j] = 0
#        mark = 1
        for k in range(len(temp)):
            if not self.judge(temp[k]):
#                mark = 0
#                break
                return False
        for q in range(len(temp[0])):
            a = []
            for p in range(len(temp)):
                a.append(temp[p][q])
            if not self.judge(a):
#                mark = 0
#                break
                return False
        for m in range(0,9,3):
            for n in range(0,9,3):
                a = []
                for p in range(m,m+3):
                    for q in range(n,n+3):
                        a.append(temp[p][q])
#                print(a,'\n')
                if not self.judge(a):
#                    mark = 0
#                    break
                    return False
#        print(temp)
        return True#mark == 1#
    
    def judge(self, nums):
        d = {}
        for k in range(len(nums)):
            try:
                d[nums[k]] += 1
            except:
                d[nums[k]] = 1
        for key, value in d.items():
#            print(k,value)
            if value != 1 and key != 0:
                return False
#        print(d)
        return True
        
    
class Solution:
def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # init data
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    boxes = [{} for i in range(9)]

    # validate a board
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3 ) * 3 + j // 3
                
                # keep the current cell value
                rows[i][num] = rows[i].get(num, 0) + 1
                columns[j][num] = columns[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                
                # check if this value has been already seen before
                if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                    return False         
    return True

#作者：LeetCode
#链接：https://leetcode-cn.com/problems/two-sum/solution/you-xiao-de-shu-du-by-leetcode/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
    
    
solu = Solution()
board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]       
#board = [
#        ["8","3",".",".","7",".",".",".","."],
#        ["6",".",".","1","9","5",".",".","."],
#        [".","9","8",".",".",".",".","6","."],
#        ["8",".",".",".","6",".",".",".","3"],
#        ["4",".",".","8",".","3",".",".","1"],
#        ["7",".",".",".","2",".",".",".","6"],
#        [".","6",".",".",".",".","2","8","."],
#        [".",".",".","4","1","9",".",".","5"],
#        [".",".",".",".","8",".",".","7","9"]
#        ]   
print(solu.isValidSudoku(board))