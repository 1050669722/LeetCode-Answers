class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        return self.stack.pop()
        

    def top(self) -> int:
        try:
            return self.stack[-1]
        except:
            return None
        

    def peekMax(self) -> int:
        try:
            return max(self.stack)
        except:
            return None
        

    def popMax(self) -> int:
        try:
            ind = 0
            tmp = self.stack[0]
            for k, s in enumerate(self.stack):
                if s >= tmp:
                    ind = k
                    tmp = s
            del self.stack[ind]
            return tmp
        except:
            return None
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()