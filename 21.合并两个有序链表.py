方法一：
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        sen = head
        while(l1 or l2):
            if l1 and not l2:
                sen.next = l1
                return head
            elif l2 and not l1:
                sen.next = l2
                return head
            elif l1.val > l2.val:
                sen.next = l2
                sen = sen.next
                l2 = l2.next
            else:
                sen.next = l1
                sen = sen.next
                l1 = l1.next
        return head
方法二：
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        pre = prehead
        while(l1 and l2):
            if l1.val<l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1:
            pre.next = l1
        else:
            pre.next = l2
        return prehead.next

时间复杂度：O(n+m) 。因为每次循环迭代中，l1 和 l2 只有一个元素会被放进合并链表中， while 循环的次数等于两个链表的总长度。所有其他工作都是常数级别的，所以总的时间复杂度是线性的。
空间复杂度：O(1) 。迭代的过程只会产生几个指针，所以它所需要的空间是常数级别的。

方法三：
我们可以如下递归地定义在两个链表里的 merge 操作（忽略边界情况，比如空链表等）：
{ list1[0]+merge(list1[1:],list2)    list1[0]<list2[0]
  list2[0]+merge(list1,list2[1:])    otherwise}
也就是说，两个链表头部较小的一个与剩下元素的 merge 操作结果合并。
我们直接将以上递归过程建模，首先考虑边界情况。
特殊的，如果 l1 或者 l2 一开始就是 null ，那么没有任何操作需要合并，所以我们只需要返回非空链表。
否则，我们要判断 l1 和 l2 哪一个的头元素更小，然后递归地决定下一个添加到结果里的值。如果两个链表都是空的，那么过程终止，所以递归过程最终一定会终止。
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
时间复杂度：O(n+m)。 因为每次调用递归都会去掉 l1 或者 l2 的头元素（直到至少有一个链表为空），函数 mergeTwoList 中只会遍历每个元素一次。所以，时间复杂度与合并后的链表长度为线性关系。
空间复杂度：O(n+m)。调用 mergeTwoLists 退出时 l1 和 l2 中每个元素都一定已经被遍历过了，所以 n+m 个栈帧会消耗 O(n+m) 的空间。
