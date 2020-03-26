方法一：
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
方法二：
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        pre.next = cur.next
        return head

时间复杂度 O(N) ： N 为链表长度，删除操作平均需循环 N/2 次，最差 N 次。
空间复杂度 O(1) ： cur, pre 占用常数大小额外空间。