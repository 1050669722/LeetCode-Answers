class MyStack:

    # 类内的类，也会作为类的属性
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None # 前面写下划线的变量不会被统配标识符调用 “非公有的”
        self._size = 0 # 用 O(1)的空间 换 O(n)的时间 很值得
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        tmp = self._head
        self._head = self.ListNode(x)
        self._head.next = tmp
        self._size += 1
        return None

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        ans = self._head.val
        self._head = self._head.next
        self._size -= 1
        return ans

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._head.val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self._size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()