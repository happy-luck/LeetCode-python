方法一：
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        cur = head
        num = 0
        while(cur):
            num += 1
            cur = cur.next
        cur = head
        while(num-k>0):
            num -= 1
            cur = cur.next
        return cur

方法二：双指针
算法流程：

初始化： 前指针 former 、后指针 latter ，双指针都指向头节点 head​ 。
构建双指针距离： 前指针 former 先向前走 k 步（结束后，双指针 former 和 latter 间相距 k 步）。
双指针共同移动： 循环中，双指针 former 和 latter 每轮都向前走一步，
	直至 former 走过链表尾节点时跳出（跳出后， latter 与尾节点距离为 k−1，即 latter 指向倒数第 k 个节点）。
返回值： 返回 latter 即可。

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast,slow = head,head
        for i in range(k):
            fast = fast.next
        while(fast):
            fast = fast.next
            slow = slow.next
        return slow

时间复杂度 O(N) ： N 为链表长度；总体看， former 走了 N 步， latter 走了 (N−k) 步。
空间复杂度 O(1) ： 双指针 former , latter 使用常数大小的额外空间。
