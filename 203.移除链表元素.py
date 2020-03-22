class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sen = ListNode(0)
        sen.next = head
        pre,cur = sen,head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return sen.next
时间复杂度：O(N)，只遍历了一次。
空间复杂度：O(1)。
