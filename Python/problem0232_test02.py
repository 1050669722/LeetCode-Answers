class MyQueue:

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None
        self._tail = None
        self._size = 0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self._size == 1:
            self._head.next = self.ListNode(x)
            self._tail = self._head.next
        elif self._size > 1:
            self._tail.next = self.ListNode(x)
            self._tail = self._tail.next
        else:
            self._head = self.ListNode(x)
            # self._tail = self.ListNode(x)
        self._size += 1
        return self._head        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self._head:
            ans = self._head.val
            self._head = self._head.next
            self._size -= 1
            return ans
        else:
            return None


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self._head:
            return self._head.val
        else:
            return None


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self._size == 0
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
tmp = obj.push(2)

# param_2 = obj.pop()
param_2 = obj.pop()
print(param_2)
# param_3 = obj.peek()
param_3 = obj.peek()
print(param_3)
# param_4 = obj.empty()

# print(tmp.val)
# print(tmp.next.val)