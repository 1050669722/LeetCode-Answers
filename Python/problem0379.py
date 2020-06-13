class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class PhoneDirectory: #用最基本的数据结构，比如链表，去做

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.head = ListNode(0)
        tmp = self.head
        for k in range(maxNumbers):
            tmp.next = ListNode(k)
            tmp = tmp.next
        

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.head:
            tmp = self.head.val
            self.head = self.head.next
            return tmp
        else:
            return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        tmp = self.head
        while tmp:
            if tmp.val == number:
                return True
        return False

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        tmp = self.head
        self.head = ListNode(number)
        self.head.next = tmp


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)