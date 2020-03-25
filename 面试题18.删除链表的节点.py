class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        sen = ListNode(0)
        sen.next = head
        pre= sen
        while(pre.next):
            if pre.next.val == val:
                pre.next = pre.next.next
                return sen.next
            pre = pre.next