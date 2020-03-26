方法一：
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        num = 0
        cur = head
        while(cur):
            num += 1
            cur = cur.next
        res = [0]*num
        cur = head
        for i in range(num):
            res[num-i-1] = cur.val
            cur = cur.next
        return res

方法二：
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

时间复杂度 O(N)： 入栈和出栈共使用 O(N) 时间。
空间复杂度 O(N)： 辅助栈 stack 和数组 res 共使用 O(N) 的额外空间。

方法三：
递推阶段： 每次传入 head.next ，以 head == None（即走过链表尾部节点）为递归终止条件，此时返回空列表 [] 。
回溯阶段： 利用 Python 语言特性，递归回溯时每次返回 当前 list + 当前节点值 [head.val] ，即可实现节点的倒序输出。

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []

时间复杂度 O(N)
空间复杂度 O(N)
