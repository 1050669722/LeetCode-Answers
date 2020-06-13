# class MyQueue:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stack = []
        

#     def push(self, x: int) -> None:
#         """
#         Push element x to the back of queue.
#         """
#         # 最基本的数据结构 所以还是不要调用python中list的方法了
#         tmp = []
#         for _ in range(len(self.stack)):
#             tmp.append(self.stack.pop())
#         self.stack.append(x)
#         for _ in range(len(tmp)):
#             self.stack.append(tmp.pop())
            
        

#     def pop(self) -> int:
#         """
#         Removes the element from in front of queue and returns that element.
#         """
#         return self.stack.pop()
        

#     def peek(self) -> int:
#         """
#         Get the front element.
#         """
#         return self.stack[-1]
        

#     def empty(self) -> bool:
#         """
#         Returns whether the queue is empty.
#         """
#         return self.stack == []


# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
            
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()