class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast = head
        slow = head
        for i in range(k):
            fast = fast.next
        while(fast):
            fast = fast.next
            slow = slow.next
        return slow.val