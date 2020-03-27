方法一：
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre,cur = None,head
        while cur:
            last = cur.next
            cur.next = pre
            pre = cur
            cur = last
        return pre
复杂度分析

时间复杂度：O(n)，假设 n 是列表的长度
空间复杂度：O(1)。
方法二：递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head==None or head.next==None):
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
时间复杂度：O(n)，假设 n 是列表的长度
空间复杂度：O(n)，由于使用递归，将会使用隐式栈空间。递归深度可能会达到 n层。