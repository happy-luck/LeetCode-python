class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while head:
            num *= 2
            num += head.val
            head = head.next
        return num
时间复杂度：O(N)，其中 N 是链表中的节点个数。
空间复杂度：O(1)